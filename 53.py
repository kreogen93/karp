# Создайте файл schema.py в той же папке, где и остальные исходные коды. Опишите в нем классы UserGet,
# PostGet, FeedGet и опишите все поля, которые есть в базе данных. Учтите, что это модель pydantic, не
# SQLAlchemy - в ней надо просто описать поля, их тип и выставить orm_mode = True.
import datetime
from pydantic import BaseModel

class UserGet(BaseModel):
    id: int
    gender: int
    age: int
    country: str
    city: str
    exp_group: int
    os: str
    source: str

    # обратите внимание: объявлен класс внутри класа
    # и в этом классе объявлены поля с нужными названиями
    # все это - часть магии FastAPI
    class Config:
        orm_mode = True


class PostGet(BaseModel):
    id: int
    text: str
    topic: str

    class Config:
        orm_mode = True


class FeedGet(BaseModel):
    user_id: int
    post_id: int
    action: str
    time: datetime.datetime

    class Config:
        orm_mode = True
