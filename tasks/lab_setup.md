Step to install the utilities

sudo apt update -y
sudo apt install -y docker.io
sudo usermod -aG docker $USER
docker --version

# Kubernetes (minikube)
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
minikube version

# kubectl
sudo snap install kubectl --classic
kubectl version --client

# Helm
sudo snap install helm --classic
helm version

# Terraform
sudo snap install terraform --classic
terraform version

# Git
sudo apt install git -y
git --version


installation verification

docker --version
minikube version
kubectl version --client
helm version
terraform version
git --version

minikube start --driver=docker

#Namespace Creation

kubectl create namespace bmw-techworks-env
kubectl config set-context --current --namespace=bmw-techworks-env

#Helm - bitnami

helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update

helm search repo bitnami/nginx

#output

NAME                                    CHART VERSION   APP VERSION     DESCRIPTION                     
bitnami/nginx                           22.3.3          1.29.3          NGINX Open Source is a web server that can be a...
bitnami/nginx-ingress-controller        12.0.7          1.13.1          NGINX Ingress Controller is an Ingress controll...
bitnami/nginx-intel                     2.1.15          0.4.9           DEPRECATED NGINX Open Source for Intel is a lig...

