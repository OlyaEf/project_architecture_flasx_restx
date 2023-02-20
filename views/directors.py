# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

from flask_restx import Resource, Namespace

from dao.model.director import directors_schema, director_schema
from implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorView(Resource):
    def get(self):
        """
        Выводит всех режиссеров.
        :return: Возвращает всех режиссеров из БД.
        """
        all_dir = director_service.get_all()
        return directors_schema.dump(all_dir), 200


@director_ns.route('/<int:uid>')
class DirectorView(Resource):
    def get(self, uid: int):
        """
        Выводит режиссера по id.
        :param uid: Идентификационный номер режиссера.
        :return: Возвращает режиссера по id.
        """
        one_dir = director_service.get_one(uid)
        return director_schema.dump(one_dir), 200
