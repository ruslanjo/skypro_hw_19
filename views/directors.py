from flask import request
from flask_restx import Resource, Namespace
from dao.model.director import DirectorSchema
from implemented import director_service
from helpers.auth_decorators import auth_required, admin_required

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        rs = director_service.get_all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200

    @admin_required
    def post(self):
        data = request.json
        director = director_service.create(data)
        return DirectorSchema().dump(director), 201


@director_ns.route('/<int:rid>')
class DirectorView(Resource):
    @auth_required
    def get(self, rid):
        r = director_service.get_one(rid)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200

    @admin_required
    def put(self, rid):
        req_data = request.json
        if "id" not in req_data:
            req_data["id"] = rid
        director_service.update(req_data)
        return '', 201

    @admin_required
    def delete(self, rid):
        director_service.delete(rid)
        return '', 204
