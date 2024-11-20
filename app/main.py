from fastapi import FastAPI
from utils import json_to_dict_list
import os
from typing import Optional

app = FastAPI()
# Получаем путь к JSON
path_to_json = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'films.json')


@app.get("/")
def home_page():
    return {"message": "bebra bebra bebra"}


@app.get("/films")
def get_all_films():
    return json_to_dict_list(path_to_json)


@app.get("/films/{film_id}")
def get_film_by_id(film_id: int):
    films = json_to_dict_list(path_to_json)
    return_list = []

    for film in films:
        if film["id"] == film_id:
            return_list.append(film)

    return return_list

# TODO
@app.get("/films")
def get_film_by_parameters(genre: Optional[str] = None, year: Optional[int] = None, imdb_rating: Optional[str] = None):
    return {"message": "Это надо сделать будет короче но потом"}


