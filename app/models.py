from enum import Enum
from pydantic import BaseModel, EmailStr, Field, field_validator, ValidationError
from datetime import date, datetime
from typing import Optional
import re


class Genre(BaseModel):
    genre_id: int
    name: str = Field(..., min_length=1, max_length=50, description="Название жанра от 1 до 50 символов")


class Review(BaseModel):
    review_id: int
    user_id: int
    film_id: int
    rating: int = Field(..., ge=1, le=10, description="Оценка фильма от 1 до 10")
    comment: Optional[str] = Field(default=None, max_length=500, description="Текст рецензии, не более 500 символов")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class Favorite(BaseModel):
    user_id: int
    film_id: int


class Watchlist(BaseModel):
    user_id: int
    film_id: int
