from dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, genre_d):
        return self.dao.create(genre_d)

    def update(self, genre_data):
        genre = self.get_one(genre_data.get("id"))
        genre.name = genre_data.get("name")
        self.dao.update(genre)
        return self.dao

    def delete(self, rid):
        self.dao.delete(rid)
