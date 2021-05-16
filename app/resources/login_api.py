from flask import  request, abort
from flask_restful import Resource
from models.users import User, UserValidationException
from global_instances import bcrypt
from flask_jwt_extended import create_access_token


class LoginApi(Resource):
    """handles login end point"""

    def verify_login(self, username, password):
        user = User.query.filter_by(username=username).first()
        if user:
            return bcrypt.check_password_hash(user.password, password)
        return False

    def post(self):
        try:
            body = request.get_json()
            User.validate_json(body)
            username = body["username"]
            password = body["password"]
            if not self.verify_login(username, password):
                return {"message": "Invalid credentials"}, 401
            access_token = create_access_token(username)
            return {"message":"Login Success", "token":access_token}, 200
        except UserValidationException as e:
            return {"message":str(e)}, 400
        except:
            abort(500)
