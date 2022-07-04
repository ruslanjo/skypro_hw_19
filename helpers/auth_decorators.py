from flask import request, abort
import jwt
from constants import SECRET, ALGO


def auth_required(func):
    def inner(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401, 'unathorized')

        token = request.headers['Authorization']

        token = token.split('Bearer ')[-1]
        try:
            jwt.decode(jwt=token, key=SECRET, algorithms=[ALGO])

        except jwt.DecodeError as e:
            abort(401, str(e))

        return func(*args, **kwargs)

    return inner


def admin_required(func):
    def inner(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401, 'unathorized')

        token = request.headers['Authorization']

        token = token.split('Bearer ')[-1]
        try:
            user_data = jwt.decode(jwt=token, key=SECRET, algorithms=[ALGO])
            if user_data.get('role') != 'admin':
                abort(400, 'admin role is required')

        except jwt.DecodeError as e:
            abort(401, str(e))

        return func(*args, **kwargs)

    return inner


