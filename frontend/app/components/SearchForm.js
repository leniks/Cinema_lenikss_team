'use client'

import { useState } from 'react';
import MovieList from '/Users/annastarostina/Downloads/yourcinema-app/frontend/app/components/MovieList.js';

export default function Search({ movies }) {
    const [searchTerm, setSearchTerm] = useState('');
    const [searchResults, setSearchResults] = useState(null); // Изменили на null
  
    const handleSearch = () => {
      const results = movies.filter((movie) =>
        movie.title.toLowerCase().includes(searchTerm.toLowerCase())
      );
      setSearchResults(results.length > 0 ? results : []); // Условие для пустого массива
    };
  
    return (
      <div id="search-container">
        <input
          type="text"
          placeholder="Название фильма"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          style={{ width: '300px' }} // Увеличили ширину поля ввода
        />
        <button onClick={handleSearch}>Найти</button>
        {searchResults === null ? null : // Не показываем ничего пока не был выполнен поиск
         (searchResults.length > 0 ? (
          <MovieList movies={searchResults} />
        ) : (
          <p>Фильм не найден.</p>
        ))}
      </div>
    );
}