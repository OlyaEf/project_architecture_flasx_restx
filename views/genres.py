# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

from flask_restx import Resource, Namespace

from dao.model.genre import genres_schema
from implemented import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenreView(Resource):
    def get(self):
        """
        Выводит все жанры.
        :return: Возвращает все жанры из БД.
        """
        all_gen = genre_service.get_all()
        return genres_schema.dump(all_gen), 200


@genre_ns.route('/<int:uid>')
class GenreView(Resource):
    def get(self, uid: int):
        """
        Выводит жанр по id.
        :param uid: Идентификационный номер жанра.
        :return: Возвращает жанр из БД.
        """
        one_gen = genre_service.get_one(uid)
        return genres_schema.dump(one_gen), 200
