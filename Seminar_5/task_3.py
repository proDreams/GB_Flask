# Создать API для добавления нового пользователя в базу данных.
# Приложение должно иметь возможность принимать POST запросы с данными нового пользователя и сохранять их в базу данных.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте маршрут для добавления нового пользователя (метод POST).
# Реализуйте валидацию данных запроса и ответа.
import pydantic
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from starlette.requests import Request
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='./templates')

users = []


class User(BaseModel):
    id_: int
    name: str
    email: pydantic.EmailStr
    password: pydantic.SecretStr


@app.get('/')
def index(request: Request):
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})


@app.get('/users/')
async def all_users():
    return {'users': users}


@app.post('/users/add')
async def add_users(user: User):
    users.append(user)
    return {"user": user, "status": "added"}


@app.put('/users/update/{user_id}')
async def update_user(user_id: int, new_user_data: User):
    for user in users:
        if user.id_ == user_id:
            user.id_ = new_user_data.id_
            user.name = new_user_data.name
            user.email = new_user_data.email
            user.password = new_user_data.password
            return {"user": user, "status": "updated"}
    return HTTPException(404, 'User not found')


@app.delete('/users/delete/{user_id}')
async def delete_user(user_id: int):
    for user in users:
        if user.id_ == user_id:
            users.remove(user)
            return {"status": "success"}
    return HTTPException(404, 'User not found')


if __name__ == "__main__":
    uvicorn.run("task_3:app", port=8001)
