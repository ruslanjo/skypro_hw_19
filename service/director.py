from dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, director_data):
        return self.dao.create(director_data)

    def update(self, director_data):
        director = self.get_one(director_data.get("id"))
        director.name = director_data.get("name")
        self.dao.update(director)
        return director

    def delete(self, rid):
        self.dao.delete(rid)