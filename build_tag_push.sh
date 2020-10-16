sudo docker build -t eliranw/actionserver:0.0.1 .
sudo docker push eliranw/actionserver:0.0.1
kubectl get pod | grep app | cut -d " " -f1 | xargs kubectl delete pod
kubectl get pods
