# Напишите endpoint GET /, т.е. который будет слушать корень "/" сайта и метод GET.
# Endpoint должен возвращать строку "hello, world".
# Используйте для этого FastAPI.
# Вы можете проверить свой код на работоспособность через Postman. Запустите веб-сервер через команду в консоли:
# uvicorn app:app --reload --port 8899
# Затем в Postman сделайте запрос GET на http://localhost:8899/. В ответе должна придти строка "hello, world" и status code 200.
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def say_hello():
    return "hello, world"
