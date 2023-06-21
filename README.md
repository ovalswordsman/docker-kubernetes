# Docker

<b>1.</b>Write a simple airflow dag to connect with db(postgres) and add entry in db for each execution (Time of dag execution)
Creating a dag with task of creating a table and inserting the value in the table
```
with DAG(dag_id='dag1', start_date=datetime(2022, 1, 1),schedule_interval='@daily',  catchup=False) as dag:
    create_table = PostgresOperator(
    task_id='create_table',
    postgres_conn_id='postgres',
    sql='''
        CREATE TABLE IF NOT EXISTS execution(
           execution_time timestamp NOT NULL
        );
    '''
    )
    # Define the PythonOperator
    add_entry_task = PythonOperator(
        task_id='add_entry_task',
        python_callable=add_entry_to_postgres,
        dag=dag
    )
 ```
<b>2.</b>Connection with db(Postgres) and entry for each execution
```
def add_entry_to_postgres():
    # Connect to the PostgreSQL database
    engine = create_engine('postgresql+psycopg2://airflow:airflow@postgres/airflow')

    # Get the current time
    current_time = datetime.now()

    # Add an entry to the database with the current time
    with engine.connect() as connection:
        connection.execute(f"INSERT INTO execution (execution_time) VALUES ('{current_time}')")
```
<b>3.</b>Use docker compose to launch airflow and postgres
```
docker-compose up -d
```
<img width="1072" alt="Screenshot 2023-05-11 at 12 31 34 PM" src="https://github.com/ovalswordsman/docker-kubernetes/assets/54627996/a78a793d-e75f-4a95-8a87-b7c8ae1c6090">

<b>4.</b>Schedule the dag
<img width="1440" alt="Screenshot 2023-05-11 at 12 32 26 PM" src="https://github.com/ovalswordsman/docker-kubernetes/assets/54627996/ecd29818-d443-475f-8820-9ad7f9712d1f">

Validate entry in postgres<br>
<br>
<br>
<img width="402" alt="Screenshot 2023-05-11 at 12 33 04 PM" src="https://github.com/ovalswordsman/docker-kubernetes/assets/54627996/d2fc0132-2e6c-4176-8461-f7413daf786a">


# Kubernetes
<b>1.</b> Installed minikube
```
brew install minikube
```
<b>2.</b>Started minikube
```
minikube start
```
<b>3.</b>Using the postgres-deployment.yaml file the pod containing postgres container was made. The following command was used,
```
kubectl apply -f postgres-deployment.yaml
```
<b>4.</b>Added dependencies of python and airflow in a postgres image by using the following commands inside the postgres pod.
```
apt-get -y update
apt-get  -y install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget 
wget https://www.python.org/ftp/python/3.7.12/Python-3.7.12.tgz
tar -xf Python-3.7.12.tgz
cd /Python-3.7.12
./configure --enable-optimizations
make -j $(nproc)
make altinstall
# STEPS TO INSTALL AIRFLOW VERSION 2.5.0
apt-get install libpq-dev
pip3.7 install "apache-airflow[postgres]==2.5.0" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.5.0/constraints-3.7.txt"
export AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgresql://airflow:airflow@localhost:5432/airflow
airflow db init
airflow users create -u airflow -p airflow -f kushagra -l singh -e kush2.official@gmail.com -r Admin
```

<b>5.</b>Then created a service of type clusterIP by running postgres-service.yaml to give access to postgres pods inside the cluster. The following command was used.

```
kubectl apply -f postgres-service.yaml
```

<b>6.</b>So entered the airflow scheduler container as root user using the following commands

```
minikube ssh #To login inside minikube cluster
docker exec -it -u root <container-id> /bin/bash #To get inside scheduler container
cd /opt/airflow/dags #Changed directory to dags folder

#Installed vim
apt-get update
apt-get install vim
vim my_db_dag.py #Made this file and copied my code inside it
```
<b>7.</b>Created a service of type load balancer by running airflow-service.yaml to access airflow webserver from my local system using the following command
    
```
kubectl apply -f airflow-service.yaml 
```
    
Accessed the airflow webserver by running the command minikube service airflow. Upon logging in, the dag was visible and it ran successfully.
    
    
    
