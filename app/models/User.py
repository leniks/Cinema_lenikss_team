from sqlalchemy import Integer, String, Text, Date, TIMESTAMP, ForeignKey, UniqueConstraint, Table, func, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.declarative import declarative_base

from app.database import Base, str_uniq, str_null_true


class User(Base):
    __tablename__ = 'users'

    username: Mapped[str_uniq]
    email: Mapped[str_uniq]
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)

    is_user: Mapped[bool] = mapped_column(default=True, server_default=text('true'), nullable=False)
    is_admin: Mapped[bool] = mapped_column(default=False, server_default=text('false'), nullable=False)

    reviews: Mapped[list["Review"]] = relationship("Review", back_populates="user")
    favorites: Mapped[list["Favorite"]] = relationship("Favorite", back_populates="user")
    watchlists: Mapped[list["Watchlist"]] = relationship("Watchlist", back_populates="user")
