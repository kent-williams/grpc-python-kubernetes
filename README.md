# grpc-python-kubernetes
This is a python3 gRPC service/client for testing gRPC services inside a Kubernetes cluster using NGINX ingress. 
It consist of a single service that responds with a UUID that is randomly generated at creation. The unique UUID response is useful for indicating that the responses are coming back from different instances of the service. Development was done on Ubuntu 18.04.

### Run Docker Image
```
sudo docker run --rm -p 50051:50051 --name grpc-python-service k3nt/grpc-python-service
```

### Deploy Kubernetes Cluster with NGINX Ingress
```
kubectl create -f gpd-dep.yaml
kubectl create -f gpd-svc.yaml
kubectl create -f gpd-ing.yaml
```
### TLS Ingress Rule for SSL
[TLS Cert Instructions](https://github.com/kubernetes/contrib/tree/master/ingress/controllers/nginx/examples/tls)

After you have created the SSL certificate and created the Kubernetes secret, you must create a .pem file for the client to use.

#### Concatenat TLS cert & key into pem
```
cat tls.crt tls.key > tls.pem
```

### Generate gRPC Code
```
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. getid.proto
```

