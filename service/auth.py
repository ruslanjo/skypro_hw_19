import jwt
from flask_restx import abort

from service.user import UserService
from constants import SECRET, ALGO
from helpers.utils import check_passwords_match, generate_token_time


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_token(self, username, password, is_refresh=False):

        user = self.user_service.get_by_username(username)

        if user is None:
            abort(400, 'no user with this username')

        if not is_refresh:
            # Если первичная генерация токена, то нужно проверить пароль
            # если же это получение рефреш токента, то мы можем доверять и не будем проверять пароль

            if not check_passwords_match(password, user.password): # проверяем, совпдают ли пароли
                abort(400, 'access denied')

        #формируем access и refresh токены, если все проверки пройдены успешно
        data = {"username": username,
                "password": password,
                "exp": generate_token_time(30),  # время для access_token,
                "role": user.role
                }

        access_token = jwt.encode(data, SECRET, algorithm=ALGO)

        # создание рефреш токена
        data['exp'] = generate_token_time(130)
        refresh_token = jwt.encode(data, SECRET, algorithm=ALGO)

        return {"access_token": access_token,
                "refresh_token": refresh_token}

    def update_token(self, refresh_token):
        # если рефреш токен действителен и валиден, то генерируем новую пару access-refresh
        try:
            data = jwt.decode(jwt=refresh_token, key=SECRET, algorithms=[ALGO])
        except jwt.DecodeError:
            abort(400, 'access denied')

        else:
            username = data.get('username')
            return self.generate_token(username=username, password=None, is_refresh=True)
