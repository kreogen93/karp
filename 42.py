# В этом задании потренируемся в валидации данных через модели (BaseModel из pydantic).
# В следующем задании нужно будет написать endpoint POST /user/validate,
# который будет принимать на вход JSON в формате:
# {
#   "name": <строка>,
#   "surname": <строка>,
#   "age": <число>,
#   "registration_date": <дата в формате YYYY-MM-DD>
# }
# Мы обязательно будем валидировать входные данные: ни один из ключей в JSON не должен быть пропущен
# и все они должны иметь тип, как указано выше. Для валидации воспользуемся моделями pydantic.
# В этом задании нужно написать класс User, который будет наследоваться от BaseModel из pydantic.
# Опишите в нем поля name, surname, age, registration_date, укажите их типы (через : - как вот name: str).
import datetime
from pydantic import BaseModel


class User(BaseModel):
    name: str
    surname: str
    age: int
    registration_date: datetime.date
