# Docker
<b>1.</b>Created a postgres connection<br>
<b>2.</b>The first task, named "create_table" was created. This task utilizes the Python Operator with PostgresHook, 
a component that interacts with a Postgres database.<br>
<b>3.</b>The second task, named "insert_execution_time" was created. This task also uses the Python Operator and PostgresHook. <br>
<b>4.</b>The third task, named "retrieve_data" was created. This task retrieves the data from the table<br>
<b>5.</b>the dependencies between the tasks were established<br>

# Kubernetes
<b>1.</b>Installed minikube.<br>
```
brew install minikube
minikube start
```

<b>2.</b>Created a postgres-deployment.yaml and made a pod using kubectl.<br>
```
kubectl apply -f postgres-deployment.yaml
```

<b>3.</b>Added dependencies of python and airflow in a postgres image by using the following commands inside the postgres pod.<br>


<b>4.</b>Made a postgres-service.yaml and created a service using<br>
```
kubectl apply -f postgres-service.yaml
```

<b>5.</b>Made a airflow-deployment.yaml and created a deployment using<br>
```
kubectl apply -f airflow-deployment.yaml
```

<b>6.</b>Made a airflow-service.yaml and created a service using<br>
```
kubectl apply -f airflow-service.yaml
```

<b>7.</b>Created a DAG and postgres connection and ran it to get the entries in a postgres table.<br>
