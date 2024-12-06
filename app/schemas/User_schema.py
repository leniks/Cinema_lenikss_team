from enum import Enum
from pydantic import BaseModel, EmailStr, Field, field_validator, ValidationError, ConfigDict
from datetime import date, datetime
from typing import Optional
import re


class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id: int
    username: str = Field(..., min_length=1, max_length=50, description="Имя пользователя от 1 до 50 символов")
    email: EmailStr
    hashed_password: str = Field(..., min_length=8, description="Хэшированный пароль (минимум 8 символов)")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)