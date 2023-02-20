# Это файл конфигурации приложения, здесь может храниться путь к бд, ключ шифрования, что-то еще.
# Чтобы добавить новую настройку, допишите ее в класс.

from constants import SQLITE_DB


# Пример

class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = SQLITE_DB
    SQLALCHEMY_TRACK_MODIFICATIONS = False
