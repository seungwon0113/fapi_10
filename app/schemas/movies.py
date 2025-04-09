from pydantic import BaseModel

class Movie(BaseModel):
    title : str
    playtime : int
    gemre : 