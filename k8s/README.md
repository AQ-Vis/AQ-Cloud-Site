## Deployment Commands for Kubernetes
https://www.digitalocean.com/community/tutorials/how-to-set-up-an-elasticsearch-fluentd-and-kibana-efk-logging-stack-on-kubernetes  
1. kubectl get namespaces
2. kubectl create -f kube-logging.yaml
3. kubectl get namespaces
4. kubectl create -f elasticsearch_svc.yaml
5. kubectl get services --namespace=kube-logging
6. kubectl create -f elasticsearch_svc.yaml
7. kubectl get services --namespace=kube-logging
8.
