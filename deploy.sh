#!/bin/bash

# Start Minikube
echo "Starting Minikube..."
minikube start

# Tag the image with Minikube's Docker daemon
eval $(minikube -p minikube docker-env)

# Build the Docker image
docker build --rm -t shopping-cart-image:latest .

# Check if the deployment already exists
if ! kubectl get deployment shopping-cart-deployment &> /dev/null; then
  # Apply the Kubernetes deployment
  kubectl apply -f minikubeDeployment.yaml
else
  echo "Deployment 'shopping-cart-deployment' already exists. Skipping deployment."
fi

# Check if the service already exists
if ! kubectl get service shopping-cart-service &> /dev/null; then
  # Expose the deployment as a NodePort service
  kubectl expose deployment shopping-cart-deployment --type=NodePort --name=shopping-cart-service
else
  echo "Service 'shopping-cart-service' already exists. Skipping service creation."
fi

# Get the NodePort assigned to the service
NODE_PORT=$(kubectl get svc shopping-cart-service -o jsonpath='{.spec.ports[0].nodePort}')

# Get Minikube IP
MINIKUBE_IP=$(minikube ip)

# Display the endpoint
echo "Access your Flask application at: http://${MINIKUBE_IP}:${NODE_PORT}"
