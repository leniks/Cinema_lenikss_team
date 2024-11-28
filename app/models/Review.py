from sqlalchemy import Integer, String, Text, Date, TIMESTAMP, ForeignKey, UniqueConstraint, Table, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.declarative import declarative_base

from app.models.movie_genres import movie_genres
from app.database import Base, str_uniq, str_null_true


class Review(Base):
    __tablename__ = 'reviews'

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    movie_id: Mapped[int] = mapped_column(Integer, ForeignKey('movies.id'))
    rating: Mapped[int] = mapped_column(Integer)  # рейтинг от 1 до 10
    comment: Mapped[str] = mapped_column(Text)

    user: Mapped["User"] = relationship("User", back_populates="reviews")
    movie: Mapped["Movie"] = relationship("Movie", back_populates="reviews")
