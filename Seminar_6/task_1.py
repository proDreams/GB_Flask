# Объедините студентов в команды по 2-5 человек  в сессионных залах.
# Разработать API для управления списком пользователей с использованием базы данных SQLite.
# Для этого создайте модель User со следующими полями:
# - id: int (идентификатор пользователя, генерируется автоматически)
# - username: str (имя пользователя)
# - email: str (электронная почта пользователя)
# - password: str (пароль пользователя)
#
# API должно поддерживать следующие операции:
# - Получение списка всех пользователей: GET /users/
# - Получение информации о конкретном пользователе: GET /users/{user_id}/
# - Создание нового пользователя: POST /users/
# - Обновление информации о пользователе: PUT /users/{user_id}/
# - Удаление пользователя: DELETE /users/{user_id}/
#
# Для валидации данных используйте параметры Field модели User.
# Для работы с базой данных используйте SQLAlchemy и модуль databases.
from typing import List

import databases
import sqlalchemy
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr, SecretStr

DATABASE_URL = "sqlite:///seminar_db.db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(32)),
    sqlalchemy.Column("email", sqlalchemy.String(128)),
    sqlalchemy.Column("password", sqlalchemy.String(64)),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)
metadata.create_all(engine)

app = FastAPI()


class UserIn(BaseModel):
    name: str = Field(max_length=32, title="Name", )
    email: EmailStr = Field(max_length=128, )
    password: SecretStr = Field(max_length=64, )


class User(UserIn):
    id: int


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/fake_users/{count}")
async def create_note(count: int):
    for i in range(count):
        query = users.insert().values(name=f'user{i}', email=f'mail{i}@mail.ru', password=f'{i}' * 10)
        await database.execute(query)
    return {'message': f'{count} fake users created'}


@app.get('/users/', response_model=List[User])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)


@app.get('/users/{user_id}', response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@app.post('/users/', response_model=User)
async def create_user(user: UserIn):
    # query = users.insert().values(name=user.name, email=user.email)
    query = users.insert().values(**user.model_dump())
    last_record_id = await database.execute(query)
    return {**user.model_dump(), "id": last_record_id}


@app.put('/users/{user_id}', response_model=User)
async def update_user(new_user: UserIn, user_id: int):
    query = users.update().where(users.c.id == user_id).values(**new_user.model_dump())
    await database.execute(query)
    return {**new_user.model_dump(), "id": user_id}


@app.delete('/users/{user_id}')
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {"message": "User deleted"}


if __name__ == "__main__":
    uvicorn.run("task_1:app", port=8001)
