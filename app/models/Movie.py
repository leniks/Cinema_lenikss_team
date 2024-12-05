from sqlalchemy import Integer, String, Text, Date, TIMESTAMP, ForeignKey, UniqueConstraint, Table, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.declarative import declarative_base

from app.models.movie_genres import movie_genres
from app.database import Base, str_uniq, str_null_true


# Модель фильма
class Movie(Base):
    __tablename__ = 'movies'

    title: Mapped[str_null_true]
    description: Mapped[str] = mapped_column(Text)
    release_date: Mapped[Date] = mapped_column(Date)
    duration: Mapped[int] = mapped_column(Integer)  # продолжительность в минутах
    rating: Mapped[int] = mapped_column(Integer)  # рейтинг от 1 до 10
    poster_url: Mapped[str_null_true]

    reviews: Mapped[list["Review"]] = relationship("Review", back_populates="movie")
    genres: Mapped[list["Genre"]] = relationship("Genre",
                                                 secondary=movie_genres,
                                                 back_populates="movies",
                                                 lazy='joined')
    favorites: Mapped[list["Favorite"]] = relationship("Favorite", back_populates="movie")
    watchlists: Mapped[list["Watchlist"]] = relationship("Watchlist", back_populates="movie")
