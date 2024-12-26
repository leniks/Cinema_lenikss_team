
'use client'
import { useState, useEffect } from 'react';
import dynamic from 'next/dynamic';
import React from 'react';
import styles from '/Users/annastarostina/Downloads/yourcinema-app/frontend/styles/globals.css'


const VideoPlayer = dynamic(() => import('../../components/ClientVideoPlayer'), {
    ssr: false,
});


function formatDate(dateString) {
  const options = { year: 'numeric', month: 'long', day: 'numeric' };
    const date = new Date(dateString);
  return date.toLocaleDateString(undefined, options);
}

export default function MoviePage({ params }) {
  const [movie, setMovie] = useState(null);
    const id = React.use(params).id;

  useEffect(() => {

  const fetchMovie = async () => {
    try{
        const response = await fetch(`http://localhost:8000/movies/${id}`)
          if(!response.ok){
              throw new Error(`HTTP error! status: ${response.status}`);
          }
        const data = await response.json();
        setMovie(data)
      } catch (error){
          console.error('Error during movie fetching:', error);
        }

    }
    fetchMovie();
    }, [id]);

  if (!movie) {
      return <div>Loading...</div>;
  }

  return (
      <div className={styles['movie-page']}>
           <div className={styles['video-container']}>
              <VideoPlayer src={movie.poster_url}  /> {/* Используем video_url */}
          </div>
          <div className={styles['movie-info']}>
              <h1 className={styles['movie-title']}>{movie.title}</h1>
              <p className={styles['movie-description']}>{movie.description}</p>
              <p className={styles['movie-release']}>Дата выхода: {formatDate(movie.release_date)}</p>
              <p className={styles['movie-duration']}>Длительность: {movie.duration} мин.</p>
            <p className={styles['movie-rating']}>Рейтинг: {movie.rating}</p>
          </div>
       </div>
    );
}