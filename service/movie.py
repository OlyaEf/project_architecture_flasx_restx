# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.
from dao.model.movie import movies_schema
from dao.movie import MovieDAO


class MovieService:

    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all_by_director(self, director_id):
        movies = self.dao.get_all_by_director(director_id)
        return movies_schema.dump(movies)

    def get_all_by_genre(self, genre_id):
        movies = self.dao.get_all_by_genre(genre_id)
        return movies_schema.dump(movies)

    def get_by_year(self, year):
        return self.dao.get_by_year(year)

    def create(self, data):
        return self.dao.create(data)

    def update(self, movie):
        return self.dao.update(movie)

    def delete(self, uid):
        self.dao.delete(uid)
        return '', 204
