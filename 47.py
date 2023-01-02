# В прошлых заданиях для того, чтобы возвращать данные в нужном формате, мы использовали
# RealDictCursor и ограничивали список колонок в SELECT - запросе.Но не всегда
# такой трюк получается и рано или поздно встанет вопрос - как проверять, что мы
# возвращаем значения в правильном формате. Для валидации ответа можно использовать
# те же pydantic модели. Напишите эндпойнт GET / post / {id}, который будет возвращать информацию о
# постах по их id и валидировать ответ.Для этого напишите класс PostResponse, наследующийся от
# pydantic.BaseModel, и в классе объявите поля id, text и topic с нужными типами(по аналогии
# с заданием на класс User).Добавьте orm_mode = True таким же способом, как делали на лекции(или
# в документации). Затем укажите, что функция - обработчик для endpoint(это функция, которую вы декорировали) возвращает
# тип PostResponse.Для указания типа возвращаемого значения используется синтаксис ->
# def my_func_returning_bool() -> bool:  # после -> может быть встроенный тип, а может быть класс
#     return False
# Наконец, скажите своему декоратору, чтобы валидировал возвращаемое значение против модели PostResponse:
# # было: @app.get(...)
# # станет:
# @app.get(..., response_model=PostResponse)
# def my_func(db):
#     ...
#
#     result = cursor.fetchone()
#     # было, не контролируем формат
#     # return result
#     # станет
#     return PostResponse(**result)
# Не забудьте, что обработку 404 надо делать заранее. По итогу у вас получится следующая схема
# cursor.fetchone() возвращает dict - объект, который может иметь любые ключи. PostResponse
# попытается из этого dict - объект создать объект класса PostResponse, валидируя при этом входные
# данные(т.е.данные из ловаря). Если ошибок валидации нет, то объект класса создается, затем тут же
# передается в return у функции - обработчика endpoint. FastAPI видит, что в return ушел объект из
# модели pydantic и понимает, что его надо сериализировать в JSON(превратить в JSON). FastAPI делает
# сериализацию, работая с провалидированным объектом. FastAPI возвращает ответ на запрос в формате JSON.
# Пользователь получает данные строго в том формате, в каком они описаны в классе PostReponse
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor

# взяли из прошлого задания
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

# объявляем новый класс для валидации ответа
class PostResponse(BaseModel):
    id: int
    text: str
    topic: str

# указываем класс в reponse_model
app = FastAPI()
# далее создаем endpoint аналогично предыдущим заданиям
@app.get("/post/{id}", response_model=PostResponse)
def get_user(id: int, db=Depends(get_db)):
    with db.cursor() as cursor:
        cursor.execute(
            """SELECT id, text, topic FROM "post" WHERE id=%(post_id)s""",
            {"post_id": id},
        )
        result = cursor.fetchone()
    if result is None:
        raise HTTPException(404, "post not found")
    return PostResponse(**result)
