# Приложение по поиску фильмов из базы данных

## Приложение на Flask 

***
Приложение позволяет находить фильмы 
по критериям поиска из базы данных, 
а так же удалять или изменять данные.
***

* Фильмы
* Жанры
* Режиссеры

'''

from flask import request

from flask_restx import Resource, Namespace

from dao.model.movie import movies_schema, movie_schema

from implemented import movie_service



movie_ns = Namespace('movies')


@movie_ns.route('/')
class MovieView(Resource):
    def get(self):
        dir_id = request.values.get('director_id')
        gen_id = request.values.get('genre_id')
        year = request.values.get('year')
        if dir_id:
            return movie_service.get_all_by_director(dir_id), 200
        if gen_id:
            return movie_service.get_all_by_genre(gen_id), 200
        if year:
            return movie_service.get_by_year(year), 200
        all_movie = movie_service.get_all()
        return movies_schema.dump(all_movie), 200

'''
