# src/restaurants/models.py
from src import db

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    cuisine_type = db.Column(db.String)
    number_of_seats = db.Column(db.Integer)
    average_price = db.Column(db.Float)
    contact = db.Column(db.String, nullable=False)
    operating_hours = db.Column(db.String, nullable=False)
