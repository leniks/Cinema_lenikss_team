'use client'; // Добавлено для указания, что это компонент клиентской стороны

import MovieCard from './MovieCard';
import { useState, useEffect } from 'react';

export default function WatchedList() {
  const [watchedMovies, setWatchedMovies] = useState([]);

  useEffect(() => {
    const getWatchedMovies = () => {
      const watched = JSON.parse(localStorage.getItem('watched')) || [];
      setWatchedMovies(watched);
    };

    getWatchedMovies();
  }, []);

  return (
    <div>
      <h1 className="watch-title">Просмотренное</h1>
      {watchedMovies.length > 0 ? (
        <div className="movie-list">
          {watchedMovies.map((movie) => (
            <MovieCard key={movie.id} movie={movie} />
          ))}
        </div>
      ) : (
        <p>Вы еще не посмотрели ни одного фильма :(</p>
      )}
    </div>
  );
}