from fastapi import APIRouter, HTTPException, Query
from typing import Annotated
from app.models.movies import MovieModel
from app.schemas.movies import CreateMovie, ResponseMovie, MovieParams, MovieUpdate

router = APIRouter(
    prefix="/movies",
    tags=["movies"]
)

# 영화 생성 API
@router.post("/", response_model=ResponseMovie)
async def create_movie(data: CreateMovie):
    movie = MovieModel.create(**data.model_dump())
    return movie

@router.get("/")
async def get_movies_list():
    result = MovieModel.all()
    if not result:
        raise HTTPException(status_code=404, detail="Movie not found")
    return result

@router.get("/search", response_model=list[ResponseMovie])
async def search_movies(q: Annotated[MovieParams, Query()]):
    valid_query = {key:value for key, value in q.model_dump().items() if value is not None}
    if valid_query:
        return MovieModel.filter(**valid_query)
    return MovieModel.all()

@router.put("/{movie_id}")
async def update_movie(movie_id: int, data: MovieUpdate):
    movie = MovieModel.get(id=movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    else:
        return movie.update(**data.model_dump())