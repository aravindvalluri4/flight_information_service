from flask import  request, abort
from flask_restful import Resource
from models.users import User
from global_instances import bcrypt


class SignupApi(Resource):
    """ Handles user signup requests """

    def does_user_exists(self, username):
        user = User.query.filter_by(username=username).first()
        return user != None

    def encrypt_pass(self, password):
        return bcrypt.generate_password_hash(password).decode('utf-8')

    def post(self):
        try:
            body = request.get_json()
            User.validate_json(body)
            username = body["username"]
            password = self.encrypt_pass(body["password"])
            if self.does_user_exists(username):
                return {"message": "username already taken"}, 409
            user = User(username=username, password=password)
            user.save()
            return {"message":"user created successfully"}, 201
        except UserValidationException as e:
            return {"message":str(e)}, 400
        except:
            abort(500)
