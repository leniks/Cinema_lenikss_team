const BASE_URL = 'http://localhost:8000'; // Замени на порт своего бэкенда

export const getTop100Movies = async () => {
    try {
        const response = await fetch(`${BASE_URL}/movies`);

        if (!response.ok) {
             // Проверяем статус, чтобы дать пользователю осмысленную ошибку
             let message = `Ошибка HTTP: ${response.status}`;
             try {
               const errorData = await response.json();
               message = errorData?.message || message; // Если есть детальное описание из backend
             } catch(jsonError) {
               // json не удалось распарсить, вероятно просто ответ с текстом
             }
            throw new Error(message); // Выбрасываем ошибку
        }

        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Ошибка при получении фильмов:', error);
        throw error;
    }
};


export const getMovieById = async (id) => {
    try {
        const response = await fetch(`${BASE_URL}/movies/${id}`);

        if (!response.ok) {
            if (response.status === 404) {
                return null; // Фильм не найден
            }
            // Проверяем статус, чтобы дать пользователю осмысленную ошибку
             let message = `Ошибка HTTP: ${response.status}`;
             try {
               const errorData = await response.json();
               message = errorData?.message || message; // Если есть детальное описание из backend
             } catch(jsonError) {
               // json не удалось распарсить, вероятно просто ответ с текстом
             }
            throw new Error(message); // Выбрасываем ошибку
        }


        const data = await response.json();

        return data;
    } catch (error) {
        console.error('Ошибка при получении фильма по id:', error);
        throw error;
    }
};