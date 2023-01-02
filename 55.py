# Осталось научиться раздавать feed.
# Напишите endpoint GET /user/{id}/feed, GET /post/{id}/feed, использующие ORM и возвращающие pydantic модель из ORM.
# Каждый endpoint должен принимать необязательный query-параметр limit, по умолчанию равный 10 - это количество записей,
# которое надо вернуть.
# GET /user/{id}/feed должен вернуть все действия из feed для пользователя с id = {id} (из запроса).
# GET /post/{id}/feed должен вернуть все действия из feed для поста с id = {id} (из запроса).
# Оба endpoint должны возвращать действия в порядке убывания их времени (т.е. самые свежие действия первыми).
# Если список действий будет пустым, то возвращайте 200 и пустой список (а не 404, как в случае с пользователем).
# Оба endpoint должны учитывать лимит (параметр limit).
from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import desc
from sqlalchemy.orm import Session
from database import SessionLocal
from table_user import User
from table_post import Post
from table_feed import Feed
from schema import FeedGet, PostGet, UserGet

app = FastAPI()


def get_feed(db: Session, id: int, limit: int, by_user_id: bool) -> Feed:
    tmp = db.query(Feed)
    tmp = (
        tmp.filter(Feed.user_id == id) if by_user_id else tmp.filter(Feed.post_id == id)
    )
    # актуальные вперед
    tmp = tmp.order_by(desc(Feed.time))
    # limit, как требовалось в задании
    tmp = tmp.limit(limit)
    return tmp.all()


def get_db() -> Session:
    return SessionLocal()


@app.get("/user/{id}/feed", response_model=List[FeedGet])
def handle_get_feed(
    id: int,
    limit: int = 10,
    db: Session = Depends(get_db),
) -> FeedGet:
    return get_feed(db, id, limit, by_user_id=True)


@app.get("/post/{id}/feed", response_model=List[FeedGet])
def handle_get_feed(
    id: int,
    limit: int = 10,
    db: Session = Depends(get_db),
) -> FeedGet:
    return get_feed(db, id, limit, by_user_id=False)
