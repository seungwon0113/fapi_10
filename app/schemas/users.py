from enum import Enum

from pydantic import BaseModel

class Gender(str, Enum):
    male = "male"
    female = "female"

class User(BaseModel):
    username : str
    age : int
    gender : Gender

class UserUpdate(BaseModel):
    username : str
    age : int
    gender : Gender

class UserParms(BaseModel):
    model_config = {"extra": "forbid"}

    username : str
    age : int
    gender : Gender