#Objective

 A pod is stuck in Pending.

Manually i have tainted the node with NoExecute, So that running pod is evicted from the node and status of the pod changed from Runing to Pending. 

I have added tolerations to the pod so that pod will be again scheduled on the node.

#Command Used- TAINT NODE

kubectl taint node minikube key=value:NoExecute
node/minikube tainted

bala@Ubuntu-server:~$ kubectl describe node minikube | grep Taints
Taints:             key=value:NoExecute

#Ouput

bala@Ubuntu-server:~$ kubectl get pods
NAME                             READY   STATUS    RESTARTS   AGE
backend-nginx-6b4ffd96dc-48r5c   0/1     Pending   0          36s
backend-nginx-6b4ffd96dc-zhtdn   0/1     Pending   0          36s

##########################################################################################

#TOLERATIONS-POD

tolerations:
  - key: "key"
    operator: "Exists"
    value: "value"
    effect: "NoExecute"

helm upgrade --install backend-nginx bitnami/nginx -f value.yml

 kubectl get pods -n bmw-techworks-env
NAME                             READY   STATUS    RESTARTS   AGE
backend-nginx-5c49796c4d-4rcpt   1/1     Running   0          32s
backend-nginx-5c49796c4d-p6gxq   1/1     Running   0          32s

kubectl describe pod backend-nginx-5c49796c4d-4rcpt

Tolerations:     key=value:NoExecute
                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                 node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age    From               Message
  ----    ------     ----   ----               -------
  Normal  Scheduled  2m33s  default-scheduler  Successfully assigned bmw-techworks-env/backend-nginx-5c49796c4d-4rcpt to minikube
  Normal  Pulled     2m30s  kubelet            Container image "registry-1.docker.io/bitnami/nginx:latest" already present on machine
  Normal  Created    2m29s  kubelet            Created container: preserve-logs-symlinks
  Normal  Started    2m28s  kubelet            Started container preserve-logs-symlinks
  Normal  Pulled     2m27s  kubelet            Container image "registry-1.docker.io/bitnami/nginx:latest" already present on machine
  Normal  Created    2m26s  kubelet            Created container: nginx
  Normal  Started    2m26s  kubelet            Started container nginx



