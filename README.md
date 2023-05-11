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

