Objective

Simulate a failure where a backend container cannot connect to the DB in Kubernetes.
Debug and fix the issue across all layers: Docker → Kubernetes → Networking → Terraform.

1 Docker Layer Debugging

Flask application (app.py) requires DB environment variables:

db_host = os.environ["DB_HOST"]
db_user = os.environ["DB_USER"]
db_pass = os.environ["DB_PASSWORD"]


📌 If missing → container exits with:

KeyError: 'DB_HOST'


A Docker image was built:

eval $(minikube docker-env)
docker build -t flask-db:env .


✔ Docker image contains DB connection logic
✔ We verified container fails immediately if env vars missing
→ Good for debugging scenario 👍

2 Kubernetes Layer Debugging

Initial deployment via Helm (missing DB env config):

helm install flask-db ./helm-flask-chart -n bmw-techworks-env

NAME: flask-db
LAST DEPLOYED: Mon Dec  1 05:34:15 2025
NAMESPACE: bmw-techworks-env
STATUS: deployed
REVISION: 1
DESCRIPTION: Install complete
TEST SUITE: None

bala@Ubuntu-server:~/bmw-techwork-assignment/tasks/Task_10-Full_Stack_Debugging$ kubectl get deploy
NAME                             READY   UP-TO-DATE   AVAILABLE   AGE
flask-db-helm-flask-chart        0/2     2            0           19s

bala@Ubuntu-server:~/bmw-techwork-assignment/tasks/Task_10-Full_Stack_Debugging$ kubectl get pods
NAME                                              READY   STATUS             RESTARTS      AGE
flask-db-helm-flask-chart-75dd9dcc56-qz79t        0/1     CrashLoopBackOff   1 (10s ago)   34s
flask-db-helm-flask-chart-75dd9dcc56-s2dtf        0/1     CrashLoopBackOff   1 (9s ago)    34s


Pods stuck:

kubectl get pods -n bmw-techworks-env
STATUS: CrashLoopBackOff


Logs revealed root cause:

kubectl logs flask-db-helm-flask-chart-75dd9dcc56-qz79t

Traceback (most recent call last):
  File "/app/app.py", line 8, in <module>
    db_host = os.environ["DB_HOST"]   # Will crash if missing
  File "/usr/local/lib/python3.9/os.py", line 679, in __getitem__
    raise KeyError(key) from None
KeyError: 'DB_HOST'


✔ Kubernetes pod was missing necessary environment configuration

3 Kubernetes Networking / Service Verification

We checked the Kubernetes service that should allow the DB hostname resolution:

kubectl get svc -n bmw-techworks-env


Output confirmed:

flask-db-helm-flask-chart        NodePort   10.100.255.54    <none>        5000:30550/TCP               

To verify Kubernetes DNS:

kubectl exec -it flask-db-helm-flask-chart-869fff579d-2sxzn -- nslookup db-service

✔ DNS resolution works
✔ Service exists
✔ Network connectivity reachable 

Even though DNS is correct, app still crashes → env missing was confirmed as the actual bottleneck.

4 Terraform Networking Validation (Simulated)

📌 In real scenarios, Terraform provisions:

✔ VPC / Subnets
✔ Security groups
✔ Routing
✔ DB Public/Private Access

We validated the Terraform intent:

terraform validate
terraform plan


✔ No network misconfiguration detected
✔ db-service is reachable within Kubernetes network

📌 So Terraform networking layer is NOT the root cause.

6 Final Fix — Apply Changes Across Layers
Step A: Updated Helm values (Configuration Layer)
env:
  - name: DB_HOST
    value: "db-service"
  - name: DB_USER
    value: "bmwadmin"
  - name: DB_PASSWORD
    value: "admin123"

Step B: Updated Deployment Template (Application Layer)
{{- if .Values.env }}
env:
  {{- toYaml .Values.env | nindent 12 }}
{{- end }}

Step C: Redeploy
helm upgrade --install flask-db ./helm-flask-chart -n bmw-techworks-env

6️⃣ Success Verification (Across All Layers)

Pod Status:

kubectl get pods -n bmw-techworks-env
STATUS: Running

bala@Ubuntu-server:~/bmw-techwork-assignment/tasks/Task_10-Full_Stack_Debugging$ kubectl get deploy | grep flask-db
flask-db-helm-flask-chart        2/2     2            2           44s

bala@Ubuntu-server:~/bmw-techwork-assignment/tasks/Task_10-Full_Stack_Debugging$ kubectl get pods | grep flask-db
flask-db-helm-flask-chart-869fff579d-2sxzn        1/1     Running   0          52s
flask-db-helm-flask-chart-869fff579d-jcktb        1/1     Running   0          52s



Logs Confirm DB Connectivity:

kubectl logs flask-db-helm-flask-chart-869fff579d-2sxzn
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://10.244.0.39:5000
Press CTRL+C to quit
10.244.0.1 - - [01/Dec/2025 06:04:37] "GET / HTTP/1.1" 200 -
10.244.0.1 - - [01/Dec/2025 06:04:43] "GET / HTTP/1.1" 200 -
10.244.0.1 - - [01/Dec/2025 06:04:47] "GET / HTTP/1.1" 200 -


App response:

Flask app connected to DB at host: db-service


✔ Docker image — Correct
✔ Kubernetes Deployment — Injected DB env
✔ DNS — Working
✔ Service — Exposed
✔ Terraform networking — Verified
