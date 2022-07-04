from dao.user import UserDAO
from helpers.utils import get_password_hash


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_by_username(self, username):
        return self.dao.get_by_username(username)

    def get_by_role(self, role):
        return self.dao.get_by_role(role)

    def get_by_id(self, uid):
        return self.dao.get_by_id(uid)



    def create(self, data):
        given_password = data['password']
        data['password'] = get_password_hash(given_password)

        return self.dao.create(data)

    def delete(self, uid):
        return self.dao.delete(uid)

    def update(self, uid, data):
        user = self.get_by_id(uid)

        user.username = data.get('username')
        user.password = get_password_hash(data.get('password'))
        user.role = data.get('role')

        self.dao.update(user)

        return user

    def update_partial(self, uid, data):
        user = self.get_by_id(uid)

        if 'username' in data:
            user.username = data.get('username')
        if 'password' in data:
            user.password = get_password_hash(data.get('password'))
        if 'role' in data:
            user.role = data.get('role')

        self.dao.update(user)

        return user
