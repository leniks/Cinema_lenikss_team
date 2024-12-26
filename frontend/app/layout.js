import Header from '/Users/annastarostina/Downloads/yourcinema-app/frontend/app/components/Header.js';
import { AuthProvider } from '/Users/annastarostina/Downloads/yourcinema-app/frontend/app/components/AuthContext.js';
import '/Users/annastarostina/Downloads/yourcinema-app/frontend/styles/globals.css';

export default function RootLayout({ children }) {
  return (
    <html lang="ru">
      <body>
        <Header />
        <AuthProvider>
          {children}
        </AuthProvider>
      </body>
    </html>
  );
}