from enum import Enum
from pydantic import BaseModel, EmailStr, Field, field_validator, ValidationError
from datetime import date, datetime
from typing import Optional
import re


class Genre(BaseModel):
    genre_id: int
    name: str = Field(..., min_length=1, max_length=50, description="Название жанра от 1 до 50 символов")
