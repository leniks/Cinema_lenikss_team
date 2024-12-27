import pandas as pd
import numpy as np

# Пример данных
data = {
    'film_id': [1, 2, 3, 4, 5],
    'title': ['Film A', 'Film B', 'Film C', 'Film D', 'Film E'],
    'genres': [
        ['Action', 'Thriller', 'Drama'],
        ['Romance', 'Comedy'],
        ['Action', 'Adventure', 'Fantasy'],
        ['Drama', 'Romance'],
        ['Comedy', 'Drama', 'Action']
    ]
}

df = pd.DataFrame(data)


# Преобразуем жанры в бинарный вектор
def genres_to_vector(all_genres, movie_genres):
    return [1 if genre in movie_genres else 0 for genre in all_genres]


# Собираем список всех уникальных жанров
all_genres = list(set(genre for genres in df['genres'] for genre in genres))

# Добавляем вектор жанров для каждого фильма
df['genre_vector'] = df['genres'].apply(lambda x: genres_to_vector(all_genres, x))


# Функция для объединения жанров нескольких фильмов
def combine_genre_vectors(selected_movies, df, all_genres):
    combined_vector = [0] * len(all_genres)
    for movie_title in selected_movies:
        movie_vector = df[df['title'] == movie_title]['genre_vector'].iloc[0]
        combined_vector = [max(combined_vector[i], movie_vector[i]) for i in range(len(all_genres))]
    return combined_vector


# Функция для получения рекомендаций
def recommend_movies_based_on_list(selected_movies, df=df):
    # Создаем общий вектор интересов на основе выбранных фильмов
    user_vector = combine_genre_vectors(selected_movies, df, all_genres)

    # Считаем схожесть с каждым фильмом
    similarities = []
    for idx, row in df.iterrows():
        similarity = jaccard_similarity(user_vector, row['genre_vector'])
        similarities.append((row['title'], similarity))

    # Исключаем из рекомендаций фильмы, которые уже были просмотрены
    similarities = [sim for sim in similarities if sim[0] not in selected_movies]

    # Сортируем фильмы по схожести
    similarities.sort(key=lambda x: x[1], reverse=True)

    # Возвращаем топ-3 рекомендации
    return [movie for movie, sim in similarities[:3]]


# Функция для вычисления коэффициента Жаккара
def jaccard_similarity(vector1, vector2):
    intersection = np.sum(np.minimum(vector1, vector2))
    union = np.sum(np.maximum(vector1, vector2))
    return intersection / union if union != 0 else 0


# Пример использования
watched_movies = ['Film A', 'Film C']
recommendations = recommend_movies_based_on_list(watched_movies)
print(f"Рекомендации на основе фильмов {watched_movies}: {recommendations}")
