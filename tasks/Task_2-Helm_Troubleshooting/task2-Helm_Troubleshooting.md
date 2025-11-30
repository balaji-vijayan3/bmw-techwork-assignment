# Task 2 - Helm Troubleshooting

## Objective
Investigate why custom Helm values were not being applied and verify the fix.

## Commands Used


helm get values backend-nginx -n bmw-techworks-env
helm get values backend-nginx -n bmw-techworks-env --all
helm get manifest backend-nginx -n bmw-techworks-env
helm upgrade --install backend-nginx bitnami/nginx -f value.yml -n bmw-techworks-env

I have manully scaled the replicas to 3 and using helm upgrade desired replica is maintained.

#output

/bmw-techwork-assignment$ kubectl get deploy
NAME            READY   UP-TO-DATE   AVAILABLE   AGE
backend-nginx   3/3     3            3           3h31m

kubectl scale deploy backend-nginx --replicas=3


######################################################

helm upgrade backend-nginx bitnami/nginx -f value.yml

level=WARN msg="unable to find exact version; falling back to closest available version" chart=nginx requested="" selected=22.3.3
Release "backend-nginx" has been upgraded. Happy Helming!
NAME: backend-nginx
LAST DEPLOYED: Fri Nov 28 12:09:32 2025
NAMESPACE: bmw-techworks-env
STATUS: deployed
REVISION: 2
DESCRIPTION: Upgrade complete
TEST SUITE: None
NOTES:

