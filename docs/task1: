## Steps Performed

1. Added Bitnami Helm repository
2. Created custom value.yml file
3. Installed NGINX using Helm into Kubernetes namespace
4. Verified using kubectl and curl

#command used

helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
kubectl create namespace bmw-techworks-env
kubectl config set-context --current --namespace=bmw-techworks-env
helm install backend-nginx bitnami/nginx -f value.yml
minikube service backend-nginx --url -n bmw-techworks-env

#output

helm list -A
NAME            NAMESPACE               REVISION        UPDATED                                 STATUS  CHART           APP VERSION
backend-nginx   bmw-techworks-env       1               2025-11-28 08:26:42.094976943 +0000 UTC deployednginx-22.3.3    1.29.3

minikube service backend-nginx --url -n bmw-techworks-env
http://192.168.49.2:32308
http://192.168.49.2:31298
bala@Ubuntu-server:~/bmw-techwork-assignment/docs$ curl http://192.168.49.2:32308
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>

