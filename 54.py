# Напишите endpoint GET /user/{id}, GET /post/{id}. Эти endpoint должны сделать SELECT запрос
# на соответствующие таблицы (используя ORM), отфильтровать одну запись по id и вернуть JSON
# с описанием (испольуйте response_model из FastAPI для валидации ответа сервера!).
# Если запись не найдена, то нужно вернуть 404 с любым сообщением.
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
# Для формирования запроса через ORM
from table_user import User
from table_post import Post
# Для валидации
from schema import PostGet, UserGet

app = FastAPI()


# Эти две функции будут далее вызываться внутри endpoint, получая на вход ORM-сессию БД
def get_user_by_id(db: Session, id: int) -> User:
    return db.query(User).filter(User.id == id).one_or_none()


def get_post_by_id(db: Session, id: int) -> Post:
    return db.query(Post).filter(Post.id == id).one_or_none()


def get_db() -> Session:
    return SessionLocal()


@app.get("/user/{id}", response_model=UserGet)
def handle_get_user(id: int, db: Session = Depends(get_db)) -> UserGet:
    # приняв сессию БД, вызовем функцию запроса
    user = get_user_by_id(db, id)
    # и вернем ее результат - а FastAPI автоматически провалидирует его против модели UserGet
    # переиспользуем наше знание по возврату ошибок 404 в этом примере
    if user is None:
        raise HTTPException(404, "user not found")
    return user

# Остальные endpoint-ы пишутся аналогично
@app.get("/post/{id}", response_model=PostGet)
def handle_get_post(id: int, db: Session = Depends(get_db)) -> PostGet:
    post = get_post_by_id(db, id)
    if post is None:
        raise HTTPException(404, "post not found")
    return post