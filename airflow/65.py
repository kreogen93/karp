# В лекции говорилось, что любой вывод return уходит неявно в XCom. Давайте это проверим.
# Создайте новый DAG, содержащий два PythonOperator. Первый оператор должен вызвать функцию,
# возвращающую строку "Airflow tracks everything".
# Второй оператор должен получить эту строку через XCom. Вспомните по лекции, какой должен быть ключ.
# Настройте правильно последовательность операторов.
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator


with DAG(
    'simple_dag_xcom_rv',
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

    def push_xcom(ti):
        return "Airflow tracks everything"

    t1 = PythonOperator(
        task_id='push_xcom',
        python_callable=push_xcom,
    )


    def retrieve_xcom(ti):
        # NOTE нужно использовать именно ключ "return_value" для значений из return
        print(ti.xcom_pull(key="return_value", task_ids="push_xcom"))

    t2 = PythonOperator(
        task_id='retrieve_xcom',
        python_callable=retrieve_xcom,
    )

    t1 >> t2
