# Потренируемся в подключении PostgreSQL СУБД к нашим приложениям. Для этого будем использовать таблицу
# user из базы данных startml(6 урок). Напишите endpoint GET / user / < id >, который будет
# принимать ID пользователя, искать его в БД и возвращать gender, age и city в формате
# JSON.Обратите внимание на то, как передается ID в запросе - прямо в самой строке.
# Для подключения к СУБД Postgres используйте следующие настройки хост postgres.lab.karpov.courses
# логин robot - startml - ro пароль pheiph0hahj1Vaif порт 6432
# база startml. Примеры запросов: GET / user / 205(или http: // localhost: 8899 / user / 205) даст
# {
#     "gender": 0,
#     "age": 32,
#     "city": "Dugulubgey"
# }
import datetime
from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor


app = FastAPI()


@app.get("/user/{id}")
def get_user(id: int):
    with psycopg2.connect(
        dbname="startml",
        host="postgres.lab.karpov.courses",
        user="robot-startml-ro",
        password="pheiph0hahj1Vaif",
        port=6432,
        cursor_factory=RealDictCursor,
    ) as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """SELECT gender, age, city FROM "user" WHERE id=%(user_id)s""",
                {"user_id": id},
            )
            return cursor.fetchone()

