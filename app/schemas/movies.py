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

class MovieParams(BaseModel):
    title : str
    genre : str

class MovieUpdate(BaseModel):
    title : str
    playtime : int
    genre : list[str]