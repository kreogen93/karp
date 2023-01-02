# Напишите endpoint GET /, который будет принимать два числа на вход и возвращать их сумму.
# Пример использования: GET /?a=5&b=3 вернет строку 8 и status_code=200
# Чтобы проверить у себя работоспособность, запустите сервис через uvicorn app:app --reload --port 8899,
# затем в Postman зайдите на http://localhost:8899/?a=5&b=3, должно вернуться 8. Вы можете также зайти
# по этой же ссылке в браузере и увидеть одну надпись 8 на белом фоне.
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def sum(a : int, b : int) -> int:
    return a + b

