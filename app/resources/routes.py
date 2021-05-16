from .signup_api import SignupApi
from .login_api import LoginApi
from .flights_api import FlightsApi
from .flight_api import FlightApi
from flask_restful import Api


def initialize_routes(app):
    """initializes different end points in app"""
    api = Api(app)
    # Authentication resources
    api.add_resource(SignupApi, "/api/v1/auth/signup")
    api.add_resource(LoginApi, "/api/v1/auth/login")

    # flights resources
    api.add_resource(FlightsApi, "/api/v1/flights")
    api.add_resource(FlightApi, "/api/v1/flights/<id>")
