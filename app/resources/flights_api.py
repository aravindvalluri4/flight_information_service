from flask_restful import Resource
from flask import request, abort, jsonify
from models.flights import Flight
from flask_jwt_extended import jwt_required


class FlightsApi(Resource):
    """ handles flights collection resource"""

    # todo pagination needs to be done
    @jwt_required
    def get(self):
        flights = Flight.query.all()
        return [flight.to_dict() for flight in flights], 200

    @jwt_required
    def post(self):
        try:
            body = request.get_json()
            flight = Flight(**body)
            flight.save()
            return {"message": "new flight created", "id": str(flight.id)}, 201

        except:
            abort(500)