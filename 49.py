# Используя класс Post из предыдущего степа, отберите все посты с topic = "business",
# отсортируйте их по убыванию их id и возьмите первые 10 id. Сделайте это все через ORM и sqlalchemy
# и распечатайте результат в виде списка из чисел. Например, [1, 2, 3, 4, 5]
# Дополните файл с классом Post соответствующим кодом, отгородив его от определения класса конструкцией
# if __name__ == "__main__", и отправьте итоговый python-скрипт в форму ниже.
# здесь наверху должно быть определение Post
# можно добавить кусок ниже прямо в файл table_post.py
from sqlalchemy import desc
from database import Base, SessionLocal
from sqlalchemy import Column, Integer, String, Text, desc, select


class Post(Base):
    # указываем явно имя таблицы, иначе SQLAlchemy не поймет и выдаст ошибку
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)  # используем тип Integer из SQLAlchemy, не из Python!
    text = Column(Text)
    # nullable разрешает пропускать значение в колонке
    topic = Column(String, nullable=True)

    # __repr__ даст возможность печатать объект (об этом говорили в лекции по классам)
    def __repr__(self):
        return f"{self.id} - {self.topic}"


if __name__ == "__main__":
    session = SessionLocal()
    # не обращайте внимание на переносы строк - они игнорируются внутри list comprehension
    # везде обращаемся через питоновский синтаксис (т.е. Класс.поле) - как будто абстрагируемся от SQL
    # только в одном месте явно используем SQL функцию - когда вызываем desc(...)
    print([x[0] for x in
        session.query(Post.id)
        .filter(Post.topic == "business")
        .order_by(desc(Post.id))
        .limit(10)
        .all()
       ]
    )