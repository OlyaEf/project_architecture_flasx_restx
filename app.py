# основной файл приложения. здесь конфигурируется фласк, сервисы, SQLAlchemy и все остальное что требуется для приложения.
# этот файл часто является точкой входа в приложение

from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db


from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns


# функция создания основного объекта app
def create_app(config: Config) -> Flask:
    # создаем app, называем ее application что бы оно не пересекалось с app
    application = Flask(__name__)
    # создаем конфигурацию, вызвав у нее специальный метод from_object
    application.config.from_object(config)  # это и есть наш конфиг класса class Config
    register_extensions(application)
    # Применение конфигурации которую мы настроили выше, чтобы Flask обновил ее по всему приложению.
    application.app_context().push()
    return application


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)


app = create_app(Config())
app.debug = True


if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
