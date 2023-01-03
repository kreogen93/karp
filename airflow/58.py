# Напишите DAG, который будет содержать BashOperator и PythonOperator. В функции PythonOperator примите
# аргумент ds и распечатайте его. Можете распечатать дополнительно любое другое сообщение.
# В BashOperator выполните команду pwd, которая выведет директорию, где выполняется ваш код Airflow.
# Результат может оказаться неожиданным, не пугайтесь - Airflow может запускать ваши задачи на разных машинах
# или контейнерах с разными настройками и путями по умолчанию.
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


with DAG(
    'hw_simple_dag',
    default_args={
        'depends_on_past': False,
        'email': ['airflow@example.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),  # timedelta из пакета datetime
    },
    description='A simple tutorial DAG',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2022, 1, 1),
    catchup=False,
    tags=['example'],
) as dag:

    t1 = BashOperator(
        task_id='print_date',
        bash_command='pwd',
    )

    def print_context(ds, **kwargs):
        print(kwargs)
        print(ds)
        return 'Whatever you return gets printed in the logs'


    t2 = PythonOperator(
        task_id='print_the_context',
        python_callable=print_context,
    )

    t1 >> t2
