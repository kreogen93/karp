# В прошлом примере все задачи в DAG были объявлены явно. Однако это не единственный способ задать DAG:
# можно использовать всю силу цикла for для объявления задач.
# Создайте новый DAG и объявите в нем 30 задач. Первые 10 задач сделайте типа BashOperator и выполните в них
# произвольную команду, так или иначе использующую переменную цикла (например, можете указать f"echo {i}").
# Оставшиеся 20 задач должны быть PythonOperator, при этом функция должна задействовать переменную из цикла.
# Вы можете добиться этого, если передадите переменную через op_kwargs и примете ее на стороне функции.
# Функция должна печатать "task number is: {task_number}", где task_number - номер задания из цикла.
from datetime import datetime, timedelta

from airflow import DAG
from textwrap import dedent
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator


with DAG(
    'hw_simple_dag_loop',
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

    t1 = DummyOperator(task_id='start_dag')
    t2 = DummyOperator(task_id='wait_for_all_bash_operators')
    t3 = DummyOperator(task_id="finish_dag")

    for i in range(10):
        task = BashOperator(
            task_id=f'print_date_{i}',
            bash_command=f"echo {i}"
        )
        t2 << task << t1

    def print_context(ts, run_id, **kwargs):
        print(kwargs)
        print(f"task number is: {kwargs.get('task_number')}")
        print(run_id)
        print(ts)
        return 'Whatever you return gets printed in the logs'


    for i in range(20):
        python_task = PythonOperator(
            task_id=f'print_the_context_{i}',
            python_callable=print_context,
            op_kwargs={"task_number": i}
        )
        t3 << python_task << t2
