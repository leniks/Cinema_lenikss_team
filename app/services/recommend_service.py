import pandas as pd
from sklearn.metrics import jaccard_score
import numpy as np

# Пример набора данных
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

# Функция для преобразования жанров в бинарный вектор
def genres_to_vector(all_genres, movie_genres):
    vector = [1 if genre in movie_genres else 0 for genre in all_genres]
    return vector


# Собираем список всех возможных жанров
all_genres = list(set([genre for genres in df['genres'] for genre in genres]))

# Преобразуем жанры каждого фильма в бинарный вектор
df['genre_vector'] = df['genres'].apply(lambda x: genres_to_vector(all_genres, x))


# Функция для вычисления коэффициента Жаккара между фильмами
def jaccard_similarity(movie1, movie2):
    intersection = np.sum(np.minimum(movie1, movie2))
    union = np.sum(np.maximum(movie1, movie2))
    return intersection / union if union != 0 else 0


# Функция для получения рекомендаций
def recommend_movie(movie_title, df=df):
    # Получаем вектор жанров для выбранного фильма
    movie_idx = df[df['title'] == movie_title].index[0]
    movie_vector = df.iloc[movie_idx]['genre_vector']

    # Считаем сходство с другими фильмами
    similarities = []
    for idx, row in df.iterrows():
        if row['title'] != movie_title:  # Исключаем сам фильм
            similarity = jaccard_similarity(movie_vector, row['genre_vector'])
            similarities.append((row['title'], similarity))

    # Сортируем фильмы по сходству
    similarities.sort(key=lambda x: x[1], reverse=True)

    # Возвращаем названия наиболее похожих фильмов
    return [movie for movie, sim in similarities[:3]]  # Рекомендуем 3 фильма


# Пример использования
print(recommend_movie('Film A'))
