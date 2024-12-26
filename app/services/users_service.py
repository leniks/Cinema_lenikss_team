from sqlalchemy import select
from app.database import async_session_maker
from sqlalchemy.exc import SQLAlchemyError

from app.models.Watchlist import Watchlist
from app.models.Favorite import Favorite
from app.models.User import User
from app.models.Review import Review
from app.models.Genre import Genre
from app.models.Movie import Movie

from app.services.auth_service import verify_password
from app.schemas.User_schema import EmailStr


class UserService:

    @classmethod
    async def get_user_or_none_by_email(cls, user_email: str):
        async with async_session_maker() as session:
            query = select(User).filter_by(email=user_email)
            result = await session.execute(query)
            return result.unique().scalar_one_or_none()

    @classmethod
    async def add_user(cls, username: str, email: str, hashed_password: str):
        async with async_session_maker() as session:
            async with session.begin():
                new_user = User(username=username, email=email, hashed_password=hashed_password)
                session.add(new_user)
                try:
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()
                    raise e
                return new_user

    @classmethod
    async def authenticate_user(cls, email: EmailStr, password: str):
        user = await UserService.get_user_or_none_by_email(user_email=email)
        if not user or verify_password(plain_password=password, hashed_password=user.hashed_password) is False:
            return None
        return user
