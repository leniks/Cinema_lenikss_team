from sqlalchemy import Table, Integer, ForeignKey, Column
from app.database import Base

movie_genres = Table(
    'user_watchlist',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('movie_id', Integer, ForeignKey('movies.id'), primary_key=True)
)
