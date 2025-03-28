from fastapi import APIRouter, HTTPException, FastAPI
from fastapi.encoders import jsonable_encoder

from app.models.users import UserModel
from app.schemas.users import User, UserUpdate

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/")
async def get_user_list():
    result = UserModel.all()
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        return result

@router.post("/")
async def create_user(data: User):
    user = UserModel.create(**data.model_dump())
    return user.id

# @router.get("/{username}")
# async def get_username(username: str):
#     user = UserModel.get(username=username)
#     print(user)
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user

@router.get("/{user_id}")
async def get_user(user_id: int):
    user = UserModel.get(id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}")
async def update_user(user_id: int, data: UserUpdate):
    user = UserModel.get(id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user.update(**data.model_dump())