from global_instances import db

class UserValidationException(Exception):
    pass


class User(db.Model):
    """ Users table """

    __tablename__ = 'users'

    username = db.Column(db.String(25), primary_key=True)
    password = db.Column(db.String(), nullable=False)

    def save(self, update=False):
        """ add/update user to database"""
        if not update:
            db.session.add(self)
        db.session.commit()

    @staticmethod
    def validate_json(user):
        """ expected format {"username":"abc", "password":"def"} """
        if "username" not in user:
            raise UserValidationException("username missing")
        elif "password" not in user:
            raise UserValidationException("password missing")




def create_users_schema():
    """ Creates users table if not present """
    db.create_all()
    db.session.commit()