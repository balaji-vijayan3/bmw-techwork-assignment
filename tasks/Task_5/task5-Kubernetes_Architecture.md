#kubeAPI-SERVER

kube-apiserver is the central communication hub of Kubernetes.
All components, users, and external tools interact with the cluster only through the API server.

#command used

kubectl get componentstatuses

#output

Warning: v1 ComponentStatus is deprecated in v1.19+
NAME                 STATUS    MESSAGE   ERROR
controller-manager   Healthy   ok
scheduler            Healthy   ok
etcd-0               Healthy   ok


#Key-Responsbilities
------------------------------------------------------------------------------------------|
| Role                           | Description                                            |
| ------------------------------ | ------------------------------------------------------ |
| Cluster Gateway                | Entry point for kubectl, dashboards, controllers       |
| Authentication & Authorization | Validates users, service accounts, permissions         |
| State Management               | Reads/writes entire cluster state in **etcd**          |
| Scheduling Trigger             | Notifies scheduler when new Pods need placement        |
| Node Communication             | Sends pod specs to **kubelet** running on worker nodes |
-------------------------------------------------------------------------------------------

#kube-apiserver Interactions Diagram

kube-apiserver is the brain’s communication bus — it connects users, cluster state (etcd), scheduling decisions, and node execution.
             +-----------------------+
             |       kubectl         |
             |   (User / DevOps)     |
             +-----------+-----------+
                         |
                         ▼  REST API Calls
                 +-------+--------+
                 | kube-apiserver |
                 +-------+--------+
                         | Writes/Reads Cluster State
                         ▼
                     +---+---+
                     | etcd  |
                     +---+---+
                         ▲
                         | Schedules Pod if New Deployment
                         ▼
               +---------+------------+
               |   kube-scheduler     |
               +---------+------------+
                         |
                         | Selects Node
                         ▼
                 +-------+--------+
                 |    kubelet     |
                 | (on each node) |
                 +----------------+

