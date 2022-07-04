from flask import request
from flask_restx import Resource, Namespace
from dao.model.genre import GenreSchema
from implemented import genre_service
from helpers.auth_decorators import auth_required, admin_required

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        rs = genre_service.get_all()
        res = GenreSchema(many=True).dump(rs)
        return res, 200

    @admin_required
    def post(self):
        req_data = request.json
        genre = genre_service.create(req_data)
        return GenreSchema().dump(genre), 201


@genre_ns.route('/<int:genre_id>')
class GenreView(Resource):
    @auth_required
    def get(self, genre_id):
        genre = genre_service.get_one(genre_id)
        genre_serialized = GenreSchema().dump(genre)
        return genre_serialized, 200

    @admin_required
    def delete(self, genre_id):
        genre_service.delete(genre_id)
        return '', 204

    @admin_required
    def put(self, genre_id):
        req_data = request.json
        if "id" not in req_data:
            req_data["id"] = genre_id
        genre_service.update(req_data)
        return '', 201
