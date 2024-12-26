'use client'
import Link from 'next/link';
import { useState } from 'react';
import styles from '/Users/annastarostina/Downloads/yourcinema-app/frontend/styles/globals.css'

function formatDate(dateString) {
  const options = { year: 'numeric', month: 'long', day: 'numeric' };
  const date = new Date(dateString);
  return date.toLocaleDateString(undefined, options);
}

export default function MovieCard({ movie }) {
  const [isFavorite, setIsFavorite] = useState(
    JSON.parse(localStorage.getItem('favorites'))?.includes(movie.id) || false
  );

  const toggleFavorite = () => {
    let favorites = JSON.parse(localStorage.getItem('favorites')) || [];
    if (isFavorite) {
      favorites = favorites.filter((id) => id !== movie.id);
    } else {
      favorites.push(movie.id);
    }
    localStorage.setItem('favorites', JSON.stringify(favorites));
    setIsFavorite(!isFavorite);
  };

    const addToWatched = () => {
        let watched = JSON.parse(localStorage.getItem('watched')) || [];
        if (!watched.some((watchedMovie) => watchedMovie.id === movie.id)) {
          watched.push(movie);
          localStorage.setItem('watched', JSON.stringify(watched));
        }
    };


  return (
      <div className={styles['movie-card']}>
            <div className={styles['movie-info']}> {}
                <span className={styles['movie-number']}>{movie.id}</span> {}
              <div className={styles['movie-title-container']}> {}
                <h3>{movie.title}</h3>
                <p>Дата выхода: {formatDate(movie.release_date)}</p>
                <p>Рейтинг: {movie.rating}</p>
                <p>Длительность: {movie.duration} мин.</p>
              </div>
            </div>
        <div className={styles['buttons-container']}>
          <button onClick={toggleFavorite} className={isFavorite ? `${styles['favorite-button']} ${styles['active']}` : styles['favorite-button']}>
            {isFavorite ? "Удалить из избранного" : "Добавить в избранное"}
          </button>
          <Link href={`/movie/${movie.id}`} className={styles['watch-button']} onClick={addToWatched}>
            Смотреть
          </Link>
        </div>
      </div>
  );
}