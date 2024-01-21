import requests
import time


def fetch_bitcoin_value():
    api_url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Check for HTTP errors

        bitcoin_value = response.json()['bitcoin']['usd']
        return bitcoin_value
    except Exception as e:
        print(f"Error fetching Bitcoin value: {e}")
        return None


def main():
    values = []

    while True:
        bitcoin_value = fetch_bitcoin_value()

        if bitcoin_value is not None:
            print(f"Bitcoin Value: {bitcoin_value} USD")
            values.append(bitcoin_value)

            if len(values) % 10 == 0:
                average_value = sum(values) / len(values)
                print(f"Average Value (Last 10 minutes): {average_value} USD")
                values = []  # Reset values list for the next 10 minutes

        time.sleep(60)  # Sleep for 1 minute


if __name__ == "__main__":
    main()
