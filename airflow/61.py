# Создайте новый DAG, состоящий из одного BashOperator. Этот оператор должен использовать шаблонизированную
# команду следующего вида:
# "Для каждого i в диапазоне от 0 до 5 не включительно распечатать значение ts и затем распечатать значение run_id".
# Здесь ts и run_id - это шаблонные переменные (вспомните, как в лекции подставляли шаблонные переменные).
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from textwrap import dedent


with DAG(
    "simple_dag_templates",
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

    templated_command = dedent(
        """
        {% for i in range(5) %}
            echo "{{ ts }}"
            echo "{{ run_id }}"
        {% endfor %}
        """
    )

    t1 = BashOperator(
        task_id='print_ts_task_id',
        bash_command=templated_command,
    )

