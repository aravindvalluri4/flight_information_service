from flask_restful import Resource
from flask import abort, request
from models.flights import Flight
from flask_jwt_extended import jwt_required
from global_instances import db


class FlightApi(Resource):
    """ handles flights/<id> resource"""

    @jwt_required
    def get(self, id):
        try:
            flight = Flight().query.filter_by(id=id).first()
            if flight is None:
                return {"message":"No resource found"}, 404
            return flight.to_dict(), 200
        except:
            abort(500)

    @jwt_required
    def put(self, id):
        try:
            body = request.get_json()
            updates = Flight().query.filter_by(id=id).update(body, synchronize_session=False)
            if updates == 0:
                return {"message":"No resource found"}, 404
            db.session.commit()
            return {"message": "updated successfully"}, 200

        except:
            abort(500)

    @jwt_required
    def delete(self, id):
        try:
            body = request.get_json()
            deletes = Flight().query.filter_by(id=id).delete()
            if deletes == 0:
                return {"message":"No resource found"}, 404
            db.session.commit()
            return {"message": "deleted successfully"}, 200

        except:
            abort(500)
