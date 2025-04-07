from fastapi import APIRouter, HTTPException, Query
from typing import Annotated
from app.models.users import UserModel
from app.schemas.users import User, UserUpdate, UserParms

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


# @router.get("/{user_id}")
# async def get_user(user_id: int):
#     # 검증된 id의 사용자 정보를 가져옴
#     user = UserModel.get(id=user_id)
#     if user is None:
#     # 사용자가 없을 시
#         raise HTTPException(status_code=404, detail="User not found")
#         # 사용자가 없다는 메세지
#     return user
#     # 조회된 유저 반환

@router.put("/{user_id}")
async def update_user(user_id: int, data: UserUpdate):

    user = UserModel.get(id=user_id)
    # 검증된 id의 사용자 정보를 가져옴
    if user is None:
        # 사용자가 없을 시
        raise HTTPException(status_code=404, detail="User not found")
        # 사용자가 없다는 메세지
    return user.update(**data.model_dump())
    # 수정된 사용자 새로 덮어쓰기

@router.delete("/{user_id}")
async def delete_user(user_id: int):
    user = UserModel.get(id=user_id)
    # 검증된 id의 사용자 정보를 가져옴
    if user is None:
        # 사용자가 없을 시
        raise HTTPException(status_code=404, detail="User not found")
        # 사용자가 없다는 메세지
    user.delete()
    # 사용자 삭제
    return {'detail':f'User: {user_id}, Successfully Deleted.'}
    # 사용자가 삭제 되었다는 메세지

@router.get("/search")
# fastapi 공식문서 : q가 선택적이지만 값이 주어질 때마다 값이 50 글자를 초과하지 않게 강제하려 합니다.
async def search_users(q: Annotated[UserParms, Query()]):
    valid_query = {key:value for key, value in q.model_dump().items() if value is not None}
    filter_users = UserModel.filter(**valid_query)
    if not filter_users:
        raise HTTPException(status_code=404)
    return filter_users
"""
<error>
"msg": "Input should be a valid integer, unable to parse string as an integer",
"input": "search"

사용자 id 조회에 user_id 를 int로 받는데 쿼리파라미터에서 막힘
@router.get("/{user_id}")
async def get_user(user_id: int):
    user = UserModel.get(id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
"""