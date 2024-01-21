# microsoft_assignment
Assignment Readme
This repository contains the solution for the assignment. It includes Kubernetes YAML files, scripts, and instructions for setting up and running the project.

Prerequisites:
Azure CLI
kubectl
Docker

Setup

1.Azure Resource Group and AKS Cluster:
Create a resource group:
az group create --name <resource-group-name> --location <region>

Create an AKS cluster:
az aks create --resource-group <resource-group-name> --name <aks-cluster-name> --node-count 1 --enable-addons monitoring --generate-ssh-keys

2. Configure kubectl:
Get AKS credentials
az aks get-credentials --resource-group <resource-group-name> --name <aks-cluster-name>

Verify connection
kubectl get nodes

3. Deploy Services and Ingress Controller:
Deploy Service A
kubectl apply -f service-a-deployment.yaml

Deploy Service B
kubectl apply -f service-b-deployment.yaml

Deploy Ingress Controller
kubectl apply -f ingress-controller.yaml

4. Apply Network Policy:
kubectl apply -f network-policy.yaml

5. Deploy Script/Application in Service A:

Deploy the script/application
kubectl apply -f service-a-script.yaml

6. Check Ingress External IP:

Wait for External IP to be assigned
kubectl get services -o wide -w

7. Access Services:

Service A: http://<ingress-external-ip>/service-A
Service B: http://<ingress-external-ip>/service-B
