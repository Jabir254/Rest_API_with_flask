#models.py

from datetime import datetime
from config import db,ma

class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    lname = db.column(db.String(32), unique=True)
    fname = db.column(db.String(32))
    timestamp = db.column(db.Datertime, default=datetime.utcnow, onupdate= datetime.utcnow)

class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        load_instance =True
        sqla_session = db.session

person_schema= PersonSchema()
people_schema= PersonSchema(many=True)