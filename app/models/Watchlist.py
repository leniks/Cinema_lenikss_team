from sqlalchemy import Integer, String, Text, Date, TIMESTAMP, ForeignKey, UniqueConstraint, Table, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.declarative import declarative_base

from app.models.movie_genres import movie_genres
from app.database import Base, str_uniq, str_null_true


class Watchlist(Base):
    __tablename__ = 'watchlists'

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    movie_id: Mapped[int] = mapped_column(Integer, ForeignKey('movies.id'))

    user: Mapped["User"] = relationship("User", back_populates="watchlists")
    movie: Mapped["Movie"] = relationship("Movie", back_populates="watchlists")

    __table_args__ = (UniqueConstraint('user_id', 'movie_id', name='uq_user_movie_watchlist'),)