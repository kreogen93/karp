# Напишите endpoint GET /sum_date, который будет принимать два параметра: current_date и offset.
# current_date будет иметь вид YYYY-MM-DD - это дата в формате год-месяц-день (например, 2022-01-01).
# offset будет целым числом (может быть отрицательным).
# Ваш endpoint должен провалидировать, что current_date имеет тип datetime.date (используйте подсказку типов,
# когда будете указывать список аргументов функции!) и валидировать, что offset имеет тип int.
# Затем endpoint должен прибавить к дате current_date дни в количестве offset и
# вернуть ответом строку в формате год-месяц-день.
# Пример использования:
# GET /sum_date?current_date=2008-09-15&offset=2 вернет "2008-09-17"
from fastapi import FastAPI
import datetime

app = FastAPI()


@app.get("/sum_date")
def sum(current_date : datetime, offset : int) -> int:
    return current_date + datetime.timedelta(days=offset)

