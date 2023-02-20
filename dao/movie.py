from dao.model.movie import Movie


# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_one(self, uid):
        return self.session.query(Movie).get(uid)

    # Create
    def get_all_by_director(self, director_id):
        return self.session.query(Movie).filter(Movie.director_id == director_id).all()

    def get_all_by_genre(self, genre_id):
        return self.session.query(Movie).filter(Movie.genre_id == genre_id).all()

    def get_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year).all()

    # Create (создание новой записи).
    # Создание и сохранение это логика нашего DAO
    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    # Update
    def update(self, movie):
        # добавить и записать
        self.session.query(Movie).filter(Movie.id == movie['id']).update(movie, synchronize_session='fetch')
        self.session.commit()
        return movie

    # Delete
    def delete(self, uid):
        movie = self.get_one(uid)
        self.session.delete(movie)
        self.session.commit()
