from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from sqlalchemy import create_engine

def add_entry_to_postgres():
    # Connect to the PostgreSQL database
    engine = create_engine('postgresql+psycopg2://airflow:airflow@postgres/airflow')

    # Get the current time
    current_time = datetime.now()

    # Add an entry to the database with the current time
    with engine.connect() as connection:
        connection.execute(f"INSERT INTO execution (execution_time) VALUES ('{current_time}')")


   
# Define the DAG
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

# Set the task dependencies
create_table >> add_entry_task
