import MovieList from '/Users/annastarostina/Downloads/yourcinema-app/frontend/app/components/MovieList.js';
import { getTop100Movies } from '../api/movies';

export default async function Home() {
  const movies = await getTop100Movies();

  return (
    <div>
        <h1 className="main-title">Топ 100 фильмов</h1>
        <MovieList movies={movies} location={"main"} />
    </div>
  );
}