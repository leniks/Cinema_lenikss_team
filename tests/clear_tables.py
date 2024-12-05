from datetime import datetime

import asyncio

from sqlalchemy import text, select
from sqlalchemy.util import await_only

from app.models.Watchlist import Watchlist
from app.models.Favorite import Favorite
from app.models.User import User
from app.models.Review import Review
from app.models.Genre import Genre
from app.models.Movie import Movie
import random

from app.database import async_session_maker, Base


async def clear_tables(session):
    await session.execute(text("DELETE FROM favorites"))
    await session.execute(text("DELETE FROM movie_genres"))
    await session.execute(text("DELETE FROM reviews"))
    await session.execute(text("DELETE FROM users"))
    await session.execute(text("DELETE FROM watchlists"))
    await session.execute(text("DELETE FROM movies"))
    await session.execute(text("DELETE FROM genres"))


async def fill_database():
    async with async_session_maker() as session:
        async with session.begin():
            await clear_tables(session)
            await session.commit()

if __name__ == "__main__":
    asyncio.run(fill_database())