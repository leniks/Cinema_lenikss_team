'use client'
import { createContext, useContext, useState } from 'react';
import { loginUser, registerUser } from '../api/users';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(null);

    const login = async (username, password) => {
        try {
            const data = await loginUser(username, password);
            setUser(data.username);
            localStorage.setItem('access_token', data.access_token);
            return true;
        } catch (error) {
            if (error.message === "Пользователь не найден") {
                console.error('Пользователь не найден!');
                return;
            }
        }
    };

    const register = async (username, email, password) => {
        try {
            const data = await registerUser(username, email, password);
            setUser(data.username);
            return true;
        } catch (error) {
            throw error;
        }
    };

    const logout = () => {
        setUser(null);
        localStorage.removeItem('access_token');
    };

    return (
        <AuthContext.Provider value={{ user, login, register, logout }}>
            {children}
        </AuthContext.Provider>
    );
};

export const useAuth = () => {
    return useContext(AuthContext);
};