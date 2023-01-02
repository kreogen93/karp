# В прошлом задании вы могли заметить, что при запросах GET /user/{id}/feed и GET /post/{id}/feed
# возвращались только id пользователей и id постов, но не информация по ним (имя, текст и т.п.).
# Можно ли как-то удобно подцепить эту информацию без особых усилий? Да, для этого и нужен relationship.
# Добавьте в класс Feed поля user и post, присвойте в них relationship на соответствующие таблицы.
# Затем добавьте в pydantic-класс FeedGet (он у вас лежит в schema.py) поля user и post типа UserGet,
# PostGet - это скажет pydantic, чтобы еще искал в возвращаемых объектах поля с именем user и post.
# Эти поля у нас будут (валидация пройдет), так как мы их только что прописали в ORM-класс Feed.
# Запустите свое приложение и убедитесь, что теперь вместе с id возвращаются и вложенные структуры
# с описанием пользователя. Обратите внимание, что в описание пользователя уходят те поля, которые описаны в
# UserGet - это pydantic все соединил аккуратно и понял вложенность структур. Теперь мы имеем гибкую возможность
# настраивать, что будет отдаваться на запрос и с какими полями.
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
    # это решение relationship
    user: UserGet
    post: PostGet
    ########3
    action: str
    time: datetime.datetime

    class Config:
        orm_mode = True


from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, desc, select
from sqlalchemy.orm import relationship

from database import Base, SessionLocal
from table_post import Post
from table_user import User


class Feed(Base):
    __tablename__ = "feed_action"
    user_id = Column(Integer, ForeignKey(User.id), primary_key=True)
    ## это решение relationship ##
    user = relationship(User)
    ##############################
    post_id = Column(Integer, ForeignKey(Post.id), primary_key=True)
    ## это решение relationship ##
    post = relationship(Post)
    ##############################
    action = Column(String, nullable=False, primary_key=True)
    time = Column(DateTime, nullable=False, primary_key=True)


if __name__ == "__main__":
    session = SessionLocal()
    stmt = select(Feed.action, User.id).join(User).join(Post)
    session.execute(stmt).one()
