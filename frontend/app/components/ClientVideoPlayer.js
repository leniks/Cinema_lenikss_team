'use client';
import React from 'react';

export default function ClientVideoPlayer({ src }) {
    console.log("Loading video from:", src); // Оставляем этот лог
        return (
            <div style={{ position: 'relative', paddingTop: '56.25%' }}>
                <iframe
                    style={{ position: 'absolute', top: 0, left: 0, width: '100%', height: '100%' }}
                    src={src}
                    title="YouTube video player"
                    frameBorder="0"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                    allowFullScreen
                ></iframe>
            </div>
        );
}