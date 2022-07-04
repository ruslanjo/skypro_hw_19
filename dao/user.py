from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    # CRUD implementation
    def get_all(self):
        return self.session.query(User).all()

    def get_by_username(self, username):
        return self.session.query(User).filter(User.username == username).first()

    def get_by_role(self, role):
        return self.session.query(User).filter(User.role == role).all()

    def get_by_id(self, uid):
        return self.session.query(User).get(uid)

    def create(self, data):
        user = User(**data)
        self.session.add(user)
        self.session.commit()
        return user

    def delete(self, uid):
        user = self.session.query(User).get(uid)
        self.session.delete(user)
        self.session.commit()

    def update(self, user_entity: User):
        self.session.add(user_entity)
        self.session.commit()
