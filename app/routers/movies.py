from fastapi import APIRouter

from app.models.movies import MovieModel
from app.schemas.movies import CreateMovie, ResponseMovie

router = APIRouter(
    prefix="/movies",
    tags=["movies"]
)

# 영화 생성 API
@router.post("/", response_model=ResponseMovie)
async def create_movie(data: CreateMovie):
    movie = MovieModel.create(**data.model_dump())
    return movie