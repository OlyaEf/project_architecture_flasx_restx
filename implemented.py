# файл для создания DAO и сервисов чтобы импортировать их везде
# Сервис-контейнер

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO
from service.director import DirectorService
from service.genre import GenreService
from service.movie import MovieService
from setup_db import db

# создаем_дао. Дао в качестве зависимости получает сессию.
# инициализируем_сервис. Указываем дао в качестве зависимости.
movie_dao = MovieDAO(db.session)
movie_service = MovieService(dao=movie_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(dao=director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(dao=genre_dao)
