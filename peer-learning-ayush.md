# Docker
<b>1.</b>Wrote a python script to create dag in which there were tasks: create a table and insert data into table<br>
<b>2.</b>Created a connection to connect the database to airflow<br>
<b>3.</b>Created docker-compose file with all the different services required.<br>
<b>4.</b>Started the containers.<br>
<b>5.</b>Triggered the dag and verified the data in the postgres container.<br>

# Kubernetes
<b>1.</b>Made a custom postgres image which will be used as airflow database.<br>
<b>2.</b>Add the image to minikube<br>
<b>3.</b>Created a pod using the postgres-deployment.yaml file<br>
<b>4.</b>Initialised the database<br>
<b>5.</b>Created a service using postgres-service.yaml file.<br>
<b>6.</b>Created a persistent volume to mount dag directory in airflow using volumes.yaml file.<br>
<b>7.</b>Created a service using airflow-service.yaml file.<br>
<b>8.</b>Started the airflow webserver using command: <b>minikube service airflow</b> <br>
