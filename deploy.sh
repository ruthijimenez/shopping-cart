#!/bin/bash

# Start Minikube
minikube start

# Point Docker client to the Docker daemon inside Minikube
eval $(minikube -p minikube docker-env)

# Build the Docker image
docker build -t shopping-cart .

# Create a Kubernetes deployment using the YAML file
kubectl apply -f minikubeDeployment.yaml

# Wait for the deployment to be ready
kubectl rollout status deployment/shopping-cart-deployment

echo "Deployment complete! Access the service at the following URL:"
minikube service shopping-cart-service
