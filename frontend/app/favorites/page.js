'use client'

import MovieList from '/Users/annastarostina/Downloads/yourcinema-app/frontend/app/components/MovieList.js';
import { getTop100Movies } from '../api/movies';
import { useState, useEffect } from 'react';

export default function FavoritesPage() {
    const [movies, setMovies] = useState([]);
  
    useEffect(() => {
      const fetchMovies = async () => {
        const favorites = JSON.parse(localStorage.getItem('favorites')) || [];
        const allMovies = await getTop100Movies(); // Запрос теперь внутри useEffect
        const filteredMovies = allMovies.filter((movie) =>
          favorites.includes(movie.id)
        );
        setMovies(filteredMovies);
      };
  
      fetchMovies();
    }, []);
  
    return (
        <div>
            <h1 className="fav-title">Избранное</h1>
            {movies.length > 0 ? (
                <MovieList movies={movies} />
            ) : (
                <p>У вас пока нет любимых фильмов :(</p>
            )}
        </div>
    );
}