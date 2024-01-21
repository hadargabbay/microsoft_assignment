#!/bin/bash

az login

RESOURCE_GROUP="myResourceGroup"
CLUSTER_NAME="myASKCluster"
REGION="your-region"

az group create --name $RESOURCE_GROUP --location $REGION
az aks create --resource-group $RESOURCE_GROUP --name $CLUSTER_NAME --enable-rbac --node-count 2 --enable-addons monitoring --generate-ssh-keys

# Step 3: Deploy Services A and B
kubectl apply -f service-a-deployment.yaml
kubectl apply -f service-b-deployment.yaml

kubectl apply -f ingress-controller.yaml

kubectl apply -f network-policy.yaml

kubectl apply -f service-a-script.yaml

kubectl get nodes -o wide
kubectl get services

echo "Cluster and services are deployed successfully!"
