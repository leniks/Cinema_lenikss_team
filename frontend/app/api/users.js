const BASE_URL = 'http://localhost:8000';

export const loginUser = async (username, password) => {
    try {
        const response = await fetch(`${BASE_URL}/users/login`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }), // Отправляем username и password
        });

        if (!response.ok) {
            let message = `Ошибка HTTP: ${response.status}`;
            try {
            const errorData = await response.json();
            message = errorData?.message || message;
            } catch(jsonError) {
            }
        throw new Error(message);
        }

        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Ошибка при входе:', error);
        throw error;
    }
    };

export const registerUser = async (username, email, password) => {
    try {
        const response = await fetch(`${BASE_URL}/users/register`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, email, password }),
        });

        if (!response.ok) {
            let message = `Ошибка HTTP: ${response.status}`;
            try {
            const errorData = await response.json();
            message = errorData?.message || message;
            } catch(jsonError) {
            }
        throw new Error(message);
        }

        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Ошибка при регистрации:', error);
        throw error;
    }
};