# Для работы с базой данных мы создавали подключение явно: либо на каждый запрос, либо один раз
# при старте приложения. В FastAPI есть более гибкий механизм предоставления различных сервисов -
# dependency injection. Концептуально это выглядит так: вы пишете функцию, которая возвращает объект,
# нужный для обработки endpoint, а endpoint заявляет, что ему нужен объект из некой функции.
# FastAPI изнутри себя производит состыковку, вызывает нужную функцию и передает ее результат в обработчик endpoint.
# Подробнее про это можно почитать в документации.
# Давайте попробуем переписать наше взаимодействие с базой данных на использование механизма dependency injection.
# Напишите функцию get_db(), которая будет возвращать объект psycopg2.connect. Затем перепишите свой endpoint
# GET /user/{id} на использование результата get_db() как Dependency. Это будет выглядеть в духе:
# @app.get(...)
# def my_func(db = Depends(get_db)):
#   ...
# Затем вы можете создать курсор через with db.cursor() as cursor и работать аналогичным образом.
from fastapi import FastAPI, HTTPException, Depends
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

def get_db():
    with psycopg2.connect(
            dbname="startml",
            host="postgres.lab.karpov.courses",
            user="robot-startml-ro",
            password="pheiph0hahj1Vaif",
            port=6432,
            cursor_factory=RealDictCursor,
    ) as conn:
        return conn


@app.get("/user/{id}")
def get_user(id: int, db=Depends(get_db)):
    with db.cursor() as cursor:
        cursor.execute(
            """SELECT gender, age, city FROM "user" WHERE id=%(user_id)s""",
            {"user_id": id},
        )
        result = cursor.fetchone()
    if result is None:
        raise HTTPException(404, "user not found")
    return result
