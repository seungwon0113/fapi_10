# main.py

from fastapi import FastAPI

from app.routers import movies
from app.routers import users
from app.models.users import UserModel
from app.models.movies import MovieModel

app = FastAPI()

app.include_router(users.router)
app.include_router(movies.router)

# API 테스트를 위한 더미를 생성하는 메서드 입니다.
UserModel.create_dummy()
MovieModel.create_dummy()


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=8000)