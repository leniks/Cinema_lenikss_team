import MovieCard from './MovieCard';

export default function MovieList({ movies, location }) {
    return (
        <div className="movie-list">
            {movies.map((movie) => (
            <MovieCard key={movie.id} movie={movie} location={location} />
            ))}
        </div>
    );
}