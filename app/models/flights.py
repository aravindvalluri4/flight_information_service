from global_instances import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
from .custom_serializer import CustomSerializerMixin


class FlightValidationException(Exception):
    pass


class Flight(db.Model, CustomSerializerMixin):
    """ Users table """

    __tablename__ = 'flights'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    flight_name = db.Column(db.String(25), nullable=False)
    flight_number = db.Column(db.Integer, nullable=False)
    schedule_date_time = db.Column(db.DateTime, nullable=False)
    arrival_date_time = db.Column(db.DateTime, nullable=False)
    departure = db.Column(db.String(25), nullable=False)
    destination = db.Column(db.String(25), nullable=False)
    fare = db.Column(db.Numeric(10,2), nullable=False)
    flight_duration_mins = db.Column(db.Integer, nullable=False)

    def save(self, update=False):
        if not update:
            db.session.add(self)
        db.session.commit()


def create_flights_table():
    db.create_all()
    db.session.commit()