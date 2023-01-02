# В прошлом задании можно заметить, что GET /user/1 даст нам null со status code 200.
# Кажется, что это не очень информативно: если пользователя не нашлось, стоит вернуть 404 и отдать сообщение.
# Перепишите endoint из прошлого задания так, чтобы он возвращал status code 404 и JSON
# {
#   "detail": "user not found"
# }
# Пример: GET /user/10 вернет status code 404 и JSON {"detail": "user not found"} (как показано выше)
from fastapi import FastAPI, HTTPException
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
            result = cursor.fetchone()
    if result is None:
        raise HTTPException(404, "user not found")
    return result
