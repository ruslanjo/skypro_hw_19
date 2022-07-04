import json

from flask import request, jsonify
from flask_restx import Namespace, Resource
from implemented import auth_service
from dao.model.user import UserSchema


user_schema = UserSchema()
users_schema = UserSchema(many=True)

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):
    def get(self):
        req_data = request.json

        username = req_data.get('username')
        password = req_data.get('password')

        if None in [username, password]:
            return '', 400

        tokens = auth_service.generate_token(username, password)
        return json.dumps(tokens), 200

    def put(self):

        data = request.json
        refresh_token = data.get('refresh_token')

        tokens = auth_service.update_token(refresh_token)

        return json.dumps(tokens), 201
