'use client'

import Link from 'next/link';
import Image from 'next/image';
import logo from '/public/logo.png';
import { usePathname } from 'next/navigation';

export default function Header() {

    const pathname = usePathname();

    return (
        <header>
        <div className="logo">
            <Image src={logo} alt="YourCinema Logo" width={60} height={60} />
            <div className="logo-text">
                <strong className="logo-title">YourCinema</strong>
                <span className="logo-subtitle">Твое кино, Твои правила</span>
            </div>
        </div>
        {pathname !== '/' && pathname !== '/register' && (
            <nav>
                <ul className="nav-links">
                    <li><Link href="/main">Главная</Link></li>
                    <li><Link href="/search">Поиск</Link></li>
                    <li><Link href="/favorites">Избранное</Link></li>
                    <li><Link href="/watched">Просмотренное</Link></li>
                </ul>
            </nav>
        )}
        </header>
    );
}