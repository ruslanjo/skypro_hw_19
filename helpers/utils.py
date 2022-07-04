import calendar
import datetime
import hashlib
import hmac
import base64
from constants import PWD_HASH_ITERATIONS, PWD_HASH_SALT, PWD_HASH_TYPE


def get_password_hash(password: str):
    password_hashed_bin = hashlib.pbkdf2_hmac(
        PWD_HASH_TYPE,
        password.encode('utf-8'),
        PWD_HASH_SALT,
        PWD_HASH_ITERATIONS
    )
    password_hashed_str = base64.b64encode(password_hashed_bin)

    return password_hashed_str


def check_passwords_match(password_input, password_db_hashed):
    password_input_hashed = get_password_hash(password_input)

    return hmac.compare_digest(password_input_hashed, password_db_hashed)


def generate_token_time(minutes: int) -> int:
    token_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=minutes)
    return calendar.timegm(token_time.timetuple())


# def check_username_password_in_request(func):
#     def inner(*args, **kwargs):
#         if ("username" or "password") not in kwargs['request_data']:
#             return {'error': 'no username or password'}
#         func(*args, **kwargs)
#     return inner
