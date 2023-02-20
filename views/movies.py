# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import movies_schema, movie_schema
from implemented import movie_service

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MovieView(Resource):
    def get(self):  # получение всех фильмов
        """
        Выводит все фильмы, а, так же выводит все фильмы при указании
        идентификационного номера режиссера, жанра или по году выпуска.
        :return: Возвращает все фильмы из БД.
        """
        dir_id = request.values.get('director_id')
        gen_id = request.values.get('genre_id')
        year = request.values.get('year')
        # получение всех фильмов по 'director_id'
        if dir_id:
            return movie_service.get_all_by_director(dir_id), 200
        # получение всех фильмов по 'genre_id'
        if gen_id:
            return movie_service.get_all_by_genre(gen_id), 200
        # получение всех фильмов по 'year'
        if year:
            return movie_service.get_by_year(year), 200
        all_movie = movie_service.get_all()
        return movies_schema.dump(all_movie), 200

    def post(self):  # создание новой записи в БД
        """
        Создает новую запись в БД фильмов.
        :return: Возвращает созданную запись.
        """
        # направляем новую форму
        req_json = request.json
        # создаем пользователя через DAO используя метод create
        created_movie = movie_service.create(req_json)
        return movie_schema.dump(created_movie), 201, {'Location': f'movies/{created_movie.id}'}


@movie_ns.route('/<int:uid>')
class MovieView(Resource):
    def get(self, uid: int):  # получение по id
        """
        Вызывает фильм по его идентификационному номеру.
        :param uid: Идентификационный номер фильма.
        :return: Возвращает фильм из БД.
        """
        # получаем объект, где запись id = uid который мы получили
        movie = movie_service.get_one(uid)
        # получив сущность мы ее сериализуем и отдаем с кодом 200
        return movie_schema.dump(movie), 200

    def put(self, uid: int):  # Замена данных
        """
        Обновляет данные о фильме.
        :param uid: Идентификационный номер фильма.
        :return: Возвращает фильм из БД.
        """
        # забирает реквест в формате json
        req_jsoon = request.json
        # получаем uid
        req_jsoon['id'] = uid
        # выполняем замену через метод dao
        movie_service.update(req_jsoon)
        return '', 204

    def delete(self, uid: int):  # Удаление записи
        """
        Удаляет фильм по его id.
        :param uid: Идентификационный номер.
        :return: Возвращает пустую строку и код 204.
        """
        # Вызываем запись по методу делит из класса
        # dao куда прокидываем нащ uid
        movie_service.delete(uid)
        return '', 204