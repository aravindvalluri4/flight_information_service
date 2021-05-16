import os
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager


db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()


def initialize_global_instances(app):
    initialize_database(app)
    initialize_bcrypt(app)
    initialize_jwt(app)


def initialize_database(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = get_postgres_uri()
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)


def initialize_bcrypt(app):
    bcrypt.init_app(app)


def initialize_jwt(app):
    app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY", "1234")
    app.config['PROPAGATE_EXCEPTIONS'] = True
    jwt.init_app(app)


def get_postgres_uri():
    host = os.getenv("POSTGRES_SERVICE_HOST", "172.17.0.2")
    port = os.getenv("POSTGRES_SERVICE_PORT", "5432")
    user = os.getenv("POSTGRES_USER", "postgres")
    password = os.getenv("POSTGRES_PASSWORD", "mypass")
    db_name = os.getenv("POSTGRES_DBNAME", "postgres")
    pg_uri = "postgresql://{}:{}@{}:{}/{}"
    return pg_uri.format(user,password,host,port,db_name)

