from sqlalchemy import Integer, String, Text, Date, TIMESTAMP, ForeignKey, UniqueConstraint, Table, func, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.declarative import declarative_base

from app.database import Base, str_uniq, str_null_true

from app.models.user_favorites import user_favorites
from app.models.user_watchlist import user_watchlist


class User(Base):
    __tablename__ = 'users'

    username: Mapped[str_uniq]
    email: Mapped[str_uniq]
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)

    is_user: Mapped[bool] = mapped_column(default=True, server_default=text('true'), nullable=False)
    is_admin: Mapped[bool] = mapped_column(default=False, server_default=text('false'), nullable=False)

    favorites: Mapped[list["Movie"]] = relationship("Movie",
                                                 secondary=user_favorites,
                                                 back_populates="favorites_users",
                                                 lazy='joined')

    watchlists: Mapped[list["Movie"]] = relationship("Movie",
                                                 secondary=user_watchlist,
                                                 back_populates="watchlists_users",
                                                 lazy='joined')
