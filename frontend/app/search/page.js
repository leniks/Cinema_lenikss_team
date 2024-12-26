import Search from '/Users/annastarostina/Downloads/yourcinema-app/frontend/app/components/SearchForm.js';
import { getTop100Movies } from '../api/movies';

export default async function SearchPage() {
  const movies = await getTop100Movies();

  return (
    <div>
      <Search movies={movies} />
    </div>
  );
}