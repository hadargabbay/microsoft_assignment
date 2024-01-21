from flask import Flask, jsonify
import requests
import time

app = Flask(__name__)

current_btc_price = None
avg_price = None
previous_prices = []


# Function to fetch Bitcoin price from CoinGecko API
def fetch_bitcoin_price(print_output=True):
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()

        if "error" in data:
            print(f"Error fetching Bitcoin price: {data['error']['message']}")
            return False

        bitcoin_price = data["bitcoin"]["usd"]  # Bitcoin price in USD
        if print_output:
            print(f"Bitcoin price: ${bitcoin_price}")

        global current_btc_price
        current_btc_price = bitcoin_price

        if print_output:
            previous_prices.append(current_btc_price)

        if len(previous_prices) == 10:
            global avg_price
            avg_price = sum(previous_prices) / 10
            if print_output:
                print(f"Average price for the past 10 minutes: {avg_price}")
            previous_prices.clear()

        return True
    except Exception as error:
        print(f"Error fetching Bitcoin price: {error}")
        return False


@app.route('/service-a/healthz')
def health_check():
    return 'OK', 200


@app.route('/service-a/readiness')
def readiness_check():
    can_fetch = fetch_bitcoin_price(False)
    return ('OK', 200) if can_fetch else ('ERROR', 400)


@app.route('/service-a')
def get_btc_data():
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    return jsonify({'Time': now, 'Price': current_btc_price, 'Average_Price': avg_price})


fetch_bitcoin_price()
while True:
    time.sleep(60)
    fetch_bitcoin_price()

if __name__ == '__main__':
    app.run(port=80)
