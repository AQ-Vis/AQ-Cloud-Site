## Deployment Commands for Kubernetes
https://www.digitalocean.com/community/tutorials/how-to-set-up-an-elasticsearch-fluentd-and-kibana-efk-logging-stack-on-kubernetes  
1. kubectl get namespaces
2. kubectl create -f kube-logging.yaml
3. kubectl get namespaces
4. kubectl create -f elasticsearch_svc.yaml
5. kubectl get services --namespace=kube-logging
<<<<<<< HEAD
6. kubectl create -f elasticsearch_svc.yaml
7. kubectl get services --namespace=kube-logging
8.
=======
6. kubectl create -f elasticsearch_statefulset.yaml
7. kubectl rollout status sts/es-cluster --namespace=kube-logging
8. kubectl port-forward es-cluster-0 9200:9200 --namespace=kube-logging
9. kubectl create -f kibana.yaml
10. kubectl rollout status deployment/kibana --namespace=kube-logging
11. kubectl get pods --namespace=kube-logging
12. kubectl port-forward kibana-6c9fb4b5b7-plbg2 5601:5601 --namespace=kube-logging
13. kubectl create -f fluentd.yaml
>>>>>>> ba92ec54b880a6894a0df936a88434dba8c6bbbc
