from flask import Flask, request, abort
from models.users import create_users_schema
from models.flights import create_flights_table
from resources.routes import initialize_routes
from global_instances import initialize_global_instances
from flask_jwt_extended import JWTManager


def create_scheamas(app):
    with app.app_context():
        create_users_schema()
        create_flights_table()


def initialize_app():
    app = Flask(__name__)
    initialize_global_instances(app)
    create_scheamas(app)
    initialize_routes(app)
    return app


app = initialize_app()
app.run(host="0.0.0.0")
