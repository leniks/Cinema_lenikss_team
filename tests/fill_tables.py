from datetime import datetime

import asyncio

from sqlalchemy import text, select
from sqlalchemy.util import await_only

from app.models.User import User
from app.models.Genre import Genre
from app.models.Movie import Movie
import random

from app.database import async_session_maker, Base

users_data = [
    {"username": "user1", "email": "user1@example.com", "hashed_password": "hashed_password1"},
    {"username": "user2", "email": "user2@example.com", "hashed_password": "hashed_password2"},
    {"username": "user3", "email": "user3@example.com", "hashed_password": "hashed_password3"},
    {"username": "user4", "email": "user4@example.com", "hashed_password": "hashed_password4"},
    {"username": "user5", "email": "user5@example.com", "hashed_password": "hashed_password5"},
    {"username": "user6", "email": "user6@example.com", "hashed_password": "hashed_password6"},
    {"username": "user7", "email": "user7@example.com", "hashed_password": "hashed_password7"},
    {"username": "user8", "email": "user8@example.com", "hashed_password": "hashed_password8"},
    {"username": "user9", "email": "user9@example.com", "hashed_password": "hashed_password9"},
    {"username": "user10", "email": "user10@example.com", "hashed_password": "hashed_password10"},
]

movies_data = [
    {"title": "Movie 1", "description": "Description 1", "release_date": datetime.strptime("2021-01-01", '%Y-%m-%d'),
     "duration": 120, "rating": 8, "poster_url": None},
    {"title": "Movie 2", "description": "Description 2", "release_date": datetime.strptime("2021-02-01", '%Y-%m-%d'),
     "duration": 90, "rating": 7, "poster_url": None},
    {"title": "Movie 3", "description": "Description 3", "release_date": datetime.strptime("2021-03-01", '%Y-%m-%d'),
     "duration": 150, "rating": 9, "poster_url": None},
    {"title": "Movie 4", "description": "Description 4", "release_date": datetime.strptime("2021-04-01", '%Y-%m-%d'),
     "duration": 110, "rating": 6, "poster_url": None},
    {"title": "Movie 5", "description": "Description 5", "release_date": datetime.strptime("2021-05-01", '%Y-%m-%d'),
     "duration": 130, "rating": 8, "poster_url": None},
    {"title": "Movie 6", "description": "Description 6", "release_date": datetime.strptime("2021-06-01", '%Y-%m-%d'),
     "duration": 95, "rating": 7, "poster_url": None},
    {"title": "Movie 7", "description": "Description 7", "release_date": datetime.strptime("2021-07-01", '%Y-%m-%d'),
     "duration": 140, "rating": 9, "poster_url": None},
    {"title": "Movie 8", "description": "Description 8", "release_date": datetime.strptime("2021-08-01", '%Y-%m-%d'),
     "duration": 100, "rating": 5, "poster_url": None},
    {"title": "Movie 9", "description": "Description 9", "release_date": datetime.strptime("2021-09-01", '%Y-%m-%d'),
     "duration": 125, "rating": 10, "poster_url": None},
    {"title": "Movie 10", "description": "Description 10",
     "release_date": datetime.strptime("2021-10-01", '%Y-%m-%d'), "duration": 115, "rating": 6, "poster_url": None}
]

genres_data = [
    {"name": "Action"},
    {"name": "Drama"},
    {"name": "Comedy"},
    {"name": "Horror"},
    {"name": "Thriller"},
    {"name": "Romance"},
    {"name": "Sci-Fi"},
    {"name": "Fantasy"},
    {"name": "Documentary"},
    {"name": "Animation"},
]

favorites_data = [
    {"user_id": 1, 'movie_id': 1},
    {'user_id': 2, 'movie_id': 2},
    {'user_id': 3, 'movie_id': 3},
    {'user_id': 4, 'movie_id': 4},
    {'user_id': 5, 'movie_id': 5},
    {'user_id': 6, 'movie_id': 6},
    {'user_id': 7, 'movie_id': 7},
    {'user_id': 8, 'movie_id': 8},
    {'user_id': 9, 'movie_id': 9},
    {'user_id': 10, 'movie_id': 10},
]

watchlists_data = [
    {"user_id": 1, 'movie_id': 2},
    {'user_id': 2, 'movie_id': 3},
    {'user_id': 3, 'movie_id': 4},
    {'user_id': 4, 'movie_id': 5},
    {'user_id': 5, 'movie_id': 6},
    {'user_id': 6, 'movie_id': 7},
    {'user_id': 7, 'movie_id': 8},
    {'user_id': 8, 'movie_id': 9},
    {'user_id': 9, 'movie_id': 10},
    {'user_id': 10, 'movie_id': 1}
]


async def clear_tables(session):
    await session.execute(text("DELETE FROM favorites"))
    await session.execute(text("DELETE FROM movie_genres"))
    await session.execute(text("DELETE FROM users"))
    await session.execute(text("DELETE FROM watchlists"))
    await session.execute(text("DELETE FROM movies"))
    await session.execute(text("DELETE FROM genres"))


async def return_true_with_probability():
    return random.random() < 0.2  # 0.2 соответствует 20%


async def fill_database():
    async with async_session_maker() as session:
        async with session.begin():
            await clear_tables(session)
            # Заполнение пользователей
            users = []
            for user in users_data:
                new_user = User(**user)
                session.add(new_user)
                users.append(new_user)

            await session.flush()  # Сохраняем пользователей, чтобы получить их ID

            # Заполнение фильмов
            movies = []
            for movie in movies_data:
                new_movie = Movie(**movie)
                session.add(new_movie)
                movies.append(new_movie)

            await session.flush()  # Сохраняем фильмы, чтобы получить их ID

            # Заполнение жанров
            genres = []
            for genre in genres_data:
                new_genre = Genre(**genre)
                session.add(new_genre)
                genres.append(new_genre)

            await session.flush()  # Сохраняем жанры, чтобы получить их ID

            for movie in movies:
                for genre in genres:
                    if await return_true_with_probability():
                        print(f"Adding genre {genre.id} to movie {movie.id}")
                        await session.refresh(movie)
                        await session.refresh(genre)
                        movie.genres.append(genre)

            session.add(new_movie)

            await session.commit()


if __name__ == "__main__":
    asyncio.run(fill_database())
