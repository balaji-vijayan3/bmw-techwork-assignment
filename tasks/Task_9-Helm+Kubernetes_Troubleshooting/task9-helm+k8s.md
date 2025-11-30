Objective

The goal of Task-9 is to troubleshoot a microservice deployment in Kubernetes using Helm when Pods are crashing.
We identify the root cause, apply a fix using Helm overrides, and verify successful deployment.

---------------------------------------------------------------------------------------------

Problem Scenario

A Flask backend was packaged as a Docker image and deployed to Kubernetes using a custom Helm chart.
After deployment, the Pods entered a CrashLoopBackOff state.

--------------------------------------------------------------------------------------------

Step 1 — Deploy Helm Release

helm install flask-backend ./helm-flask-chart

NAME: flask-backend
LAST DEPLOYED: Sun Nov 30 09:27:47 2025
NAMESPACE: bmw-techworks-env
STATUS: deployed
REVISION: 2
DESCRIPTION: Upgrade complete

@kubeclt get deploy

NAME                             READY   UP-TO-DATE   AVAILABLE   AGE
flask-backend-helm-flask-chart   0/2     0            0           44m

@kubectl get pods

NAME                                              READY   STATUS             RESTARTS        AGE
flask-backend-helm-flask-chart-86d7995685-cmhjw   0/1     CrashLoopBackOff   15 (112s ago)   45m
flask-backend-helm-flask-chart-86d7995685-zkbp2   0/1     CrashLoopBackOff   16 (2m8s ago)   45m

Step 2 — Troubleshoot the Pod

Logs: kubectl logs flask-backend-helm-flask-chart-86d7995685-cmhjw -n bmw-techworks-env
-----------------------------------------------------------------------------------
Traceback (most recent call last):
  File "/app/app.py", line 6, in <module>
    MESSAGE = os.environ["APP_MESSAGE"]  # Will crash if APP_MESSAGE is not set
NameError: name 'os' is not defined
-----------------------------------------------------------------------------------

Application failed because the required environment variable (APP_MESSAGE) was not set inside the container.

######################################################################################################

Step 3 — Apply Fix Using Helm Values 
Updated value.yml (Added env variables)

env:
  - name: APP_MESSAGE
    value: "This is flask docker app from ENV"


Step 4 — Redeploy With Fix

@helm upgrade --install flask-backend ./helm-flask-chart

NAME: flask-backend
LAST DEPLOYED: Sun Nov 30 09:37:22 2025
NAMESPACE: bmw-techworks-env
STATUS: deployed
REVISION: 7
DESCRIPTION: Upgrade complete

@kubeclt get deploy

NAME                             READY   UP-TO-DATE   AVAILABLE   AGE
flask-backend-helm-flask-chart   2/2     2            0           8s

@kubeclt get pods

NAME                                              READY   STATUS    RESTARTS   AGE
flask-backend-helm-flask-chart-6444f54697-762sf   1/1     Running   0          40s
flask-backend-helm-flask-chart-6444f54697-kn5rk   1/1     Running   0          40s

checking logs: kubectl logs flask-backend-helm-flask-chart-6444f54697-kn5rk

 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://10.244.0.33:5000

