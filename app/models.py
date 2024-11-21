from enum import Enum
from pydantic import BaseModel, EmailStr, Field, field_validator, ValidationError
from datetime import date, datetime
from typing import Optional
import re


class Film(BaseModel):
    film_id: int
    title: str = Field(min_length=1, max_length=50, description="Название фильма, от 1 до 50 символов")
    description: Optional[str] = Field(default=None, max_length=500,
                                       description="Описание фильма, не более 500 символов")
    release_date: date = Field(description="Дата выхода фильма в формате ГГГГ-ММ-ДД")
    duration: int = Field(ge=0, description="Продолжительность в минутах")
    rating_imdb: float = Field(ge=0.0, le=10.0, description="Рейтинг фильма на IMDb")
    poster_url: str = Field(description="URL постера фильма")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    @field_validator('release_date')
    def check_release_date(cls, value):
        if value > date.today():
            raise ValueError("Дата выхода не может быть в будущем.")
        return value


class User(BaseModel):
    user_id: int
    username: str = Field(min_length=1, max_length=50, description="Имя пользователя от 1 до 50 символов")
    email: EmailStr
    hashed_password: str = Field(min_length=8, description="Хэшированный пароль (минимум 8 символов)")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class Genre(BaseModel):
    genre_id: int
    name: str = Field(min_length=1, max_length=50, description="Название жанра от 1 до 50 символов")


class Review(BaseModel):
    review_id: int
    user_id: int
    film_id: int
    rating: int = Field(ge=1, le=10, description="Оценка фильма от 1 до 10")
    comment: Optional[str] = Field(default=None, max_length=500, description="Текст рецензии, не более 500 символов")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class Favorite(BaseModel):
    user_id: int
    film_id: int


class Watchlist(BaseModel):
    user_id: int
    film_id: int
