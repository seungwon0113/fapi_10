from http.client import HTTPException

from fastapi import APIRouter

from app.models import users
from app.models.users import UserModel
from app.schemas.users import Gender

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/")
async def get_users():
    result = UserModel.all()
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    return result

@router.get("/{username}")
async def get_users(username : str, age : int, gender : Gender):
    result = UserModel.filter(username=username, age=age, gender=gender)
    return result