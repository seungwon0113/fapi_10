from pydantic import BaseModel

class CreateMovie(BaseModel):
    title : str
    playtime : int
    genre : list[str]

class ResponseMovie(BaseModel):
    id : int
    title : str
    playtime : int
    genre : list[str]