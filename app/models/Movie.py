from sqlalchemy import Integer, String, Text, Date, TIMESTAMP, ForeignKey, UniqueConstraint, Table, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.declarative import declarative_base

from app.models.movie_genres import movie_genres
from app.models.user_favorites import user_favorites
from app.models.user_watchlist import user_watchlist

from app.database import Base, str_uniq, str_null_true


# Модель фильма
class Movie(Base):
    __tablename__ = 'movies'

    title: Mapped[str_null_true]
    description: Mapped[str] = mapped_column(Text)
    release_date: Mapped[Date] = mapped_column(Date)
    duration: Mapped[int] = mapped_column(Integer)  # продолжительность в минутах
    rating: Mapped[int] = mapped_column(Integer)  # рейтинг от 1 до 10
    movie_url: Mapped[str_null_true]

    genres: Mapped[list["Genre"]] = relationship("Genre",
                                                 secondary=movie_genres,
                                                 back_populates="movies",
                                                 lazy='joined')
    favorites_users: Mapped[list["User"]] = relationship("User",
                                                 secondary=user_favorites,
                                                 back_populates="favorites",
                                                 lazy='joined')
    watchlists_users: Mapped[list["User"]] = relationship("User",
                                                 secondary=user_watchlist,
                                                 back_populates="watchlists",
                                                 lazy='joined')
