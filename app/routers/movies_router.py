from fastapi import APIRouter, Depends
from app.services.movies_service import MovieService
from typing import Optional, List
from app.schemas.Movie import SMovie

class RBMovie:
    def __init__(self, id: int | None = None,
                 title: int | None = None):
        self.id = id
        self.title = title

    def to_dict(self) -> dict:
        data = {'id': self.id, 'title': self.title}
        # Создаем копию словаря, чтобы избежать изменения словаря во время итерации
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data

router = APIRouter(prefix='/movies', tags=['Работа с фильмами '])

@router.get("/", summary="Получить все фильмы или фильмы с некоторыми параметрами", response_model=List[SMovie])
async def get_movies_by_parameters(request_body: RBMovie = Depends()):
    return await MovieService.get_movies_by_parameters(**request_body.to_dict())

@router.get("/{id}", summary="Получить фильм по id")
async def get_movie_or_none_by_id(movie_id: int) -> SMovie | None:
    return await MovieService.get_movie_or_none_by_id(movie_id)