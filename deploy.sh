#!/bin/bash

source venv/bin/activate
# Step 1: Build the Docker image using the existing Dockerfile
# Replace 'shopping-cart' with the name you want for your Docker image
docker build -t shopping-cart .

# Step 2: Tag the Docker image
# Replace '1.0.0' with the version you want for your Docker image
docker tag shopping-cart:latest shopping-cart:1.0.0

# Step 3: Set Minikube to use the local Docker daemon
eval $(minikube docker-env)

# Step 4: Deploy the Docker image to Minikube using the existing YAML file
# Replace 'minikubeDeployment.yaml' with the path to your YAML file if it's not in the current directory
kubectl apply -f minikubeDeployment.yaml

# Step 5: Expose the service to access it on localhost
# Replace 'shopping-cart' with the name of your service in the YAML file
kubectl expose deployment shopping-cart --type=LoadBalancer --port=5000
# minikube service shopping-cart

echo "Deployment complete! Access the service at the following URL:"
minikube service shopping-cart --url