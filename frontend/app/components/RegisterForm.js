'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import { useAuth } from '/Users/annastarostina/Downloads/yourcinema-app/frontend/app/components/AuthContext.js';

export default function RegisterForm() {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);
  const { register } = useAuth();
  const router = useRouter();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);

    try {
      await register(username, email, password);
      router.push('/');
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div className="auth-container">
        <div className="auth-box">
            <h1 className="auth-title">Регистрация</h1>
            <form onSubmit={handleSubmit} className="auth-form">
                <input
                type="text"
                placeholder="Username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                />
                <input
                type="email"
                placeholder="Email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                />
                <input
                type="password"
                placeholder="Пароль"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                />
                <button type="submit">Зарегистрироваться</button>
            </form>
            {error && <div className="auth-errorMessage">{error}</div>}
            
            <h1 className="auth-p">Уже есть аккаунт? <a href="/login">Войти</a></h1>

        </div>
    </div>
  );
}