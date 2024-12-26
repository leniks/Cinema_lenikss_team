'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import { useAuth } from '/Users/annastarostina/Downloads/yourcinema-app/frontend/app/components/AuthContext.js';

export default function LoginForm() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);
  const { login } = useAuth();
  const router = useRouter();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);

    try {
      await login(username, password);
      router.push('/main');
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div className="auth-container">
        <div className="auth-box">
            <h1 className="auth-title">Вход</h1>
            <form onSubmit={handleSubmit} className="auth-form">
                 <input
                type="text"
                placeholder="Username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                />
                <input
                type="password"
                placeholder="Пароль"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                />
                <button type="submit">Войти</button>
            </form>
            {error && <div className="auth-errorMessage">{error}</div>}
            
            <h1 className="auth-p">Нет аккаунта? <a href="/register">Зарегистрируйтесь</a></h1>

        </div>
    </div>
  );
}