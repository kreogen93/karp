# Оберните таблицу user в ORM по аналогии с тем, как делали с таблицей post.
# Точно так же берите Base из database (from database import Base) и используйте следующий файл database.py:


from sqlalchemy import Column, Integer, String, Text, desc, select
from sqlalchemy.sql import func
from database import Base, SessionLocal


class User(Base):
    __tablename__ = "user"
    # очень много колонок, но они все однотипные
    # нужно помнить, что int -> Integer, str -> String, и все они импортируются из sqlalchemy
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