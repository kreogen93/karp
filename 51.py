# Используя класс User из прошлого пункта, магию ORM и немного чтения документации,
# отберите всех пользователей, у которых экспериментальная группа равна 3, сгруппируйте их по парам
# (country, os) и выведите эти пары (country, os, count(*)), отсортированные по убыванию COUNT(*) и имеющие
# COUNT(*) > 100 (т.е. те пары, в которых более 100 записей). Результат сохраните в список из кортежей,
# например, [("Germany", "Android", 100), ("Russia", "iOS", 10033)], и распечатайте его.
# Дополните файл с классом User соответствующим кодом, отгородив его от определения класса конструкцией
# if __name__ == "__main__", и отправьте итоговый python-скрипт в форму ниже.
from sqlalchemy import Column, Integer, String, Text, desc, select
from sqlalchemy.sql import func

from database import Base, SessionLocal


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    gender = Column(Integer, nullable=False)
    age = Column(Integer, nullable=False)
    country = Column(String, nullable=False)
    city = Column(String, nullable=False)
    exp_group = Column(Integer, nullable=False)
    os = Column(String, nullable=False)
    source = Column(String, nullable=False)

    def __repr__(self):
        return f"{self.id}"


if __name__ == "__main__":
    session = SessionLocal()
    stmt = (
        select(User.country, User.os, func.count("*"))
        .filter(User.exp_group == 3)
        .group_by(User.country, User.os)
        .having(func.count("*") > 100)
        .order_by(desc(func.count("*")))
    )
    print(session.execute(stmt).all())
