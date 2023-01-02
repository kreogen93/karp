# У нас осталась таблица feed_action. С ней есть тонкость: в ней присутствуют ключи из других таблиц (ForeignKey).
# Оберните таблицу feed_action в ORM. Используйте названия user_id и post_id для соответствующих колонок и укажите,
# что они являются ForeignKey. Пока не делайте relationship (если уже хочется) - их оставим на следующие примеры.
# Как обычно, используйте Base из database.py, который был в прошлых степах, и импортируйте Base точно так же из database
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, desc, select
from sqlalchemy.orm import relationship

from database import Base, SessionLocal
from table_post import Post
from table_user import User


class Feed(Base):
    __tablename__ = "feed_action"
    user_id = Column(Integer, ForeignKey(User.id), primary_key=True)
    post_id = Column(Integer, ForeignKey(Post.id), primary_key=True)
    action = Column(String, nullable=False, primary_key=True)
    time = Column(DateTime, nullable=False, primary_key=True)
