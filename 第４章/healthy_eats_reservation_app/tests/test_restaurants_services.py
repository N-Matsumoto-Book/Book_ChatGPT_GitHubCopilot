import unittest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.restaurants.services import RestaurantManager
from src.restaurants.models import db, Restaurant

class RestaurantModelCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = Flask(__name__)
        cls.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        cls.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(cls.app)
        with cls.app.app_context():
            db.create_all()
        restaurants = [
            Restaurant(name='Test Restaurant 1', location='Tokyo, Japan', cuisine_type='Sushi', number_of_seats=50, average_price=30.5, contact='test1@restaurant.com', operating_hours='10:00 AM - 10:00 PM'),
            Restaurant(name='Test Restaurant 2', location='Paris, France', cuisine_type='French', number_of_seats=40, average_price=40.5, contact='test2@restaurant.com', operating_hours='11:00 AM - 10:00 PM'),
            Restaurant(name='Test Restaurant 3', location='Rome, Italy', cuisine_type='Italian', number_of_seats=45, average_price=25.0, contact='test3@restaurant.com', operating_hours='09:00 AM - 10:00 PM'),
            Restaurant(name='Test Restaurant 4', location='New York, USA', cuisine_type='Burgers', number_of_seats=60, average_price=15.5, contact='test4@restaurant.com', operating_hours='10:00 AM - 11:00 PM'),
            Restaurant(name='Test Restaurant 5', location='Berlin, Germany', cuisine_type='German', number_of_seats=55, average_price=20.0, contact='test5@restaurant.com', operating_hours='08:00 AM - 09:00 PM'),
        ]
        with cls.app.app_context():
            db.session.add_all(restaurants)
            db.session.commit()

    @classmethod
    def tearDownClass(cls):
        with cls.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_search_with_location_and_cuisine_type(self):
        with self.app.app_context():
            restaurants = RestaurantManager.get_restaurants_by_criteria(location='Tokyo', cuisine_type='Sushi')
            self.assertEqual(len(restaurants), 1)
            self.assertEqual(restaurants[0].name, 'Test Restaurant 1')

    def test_search_with_location(self):
        with self.app.app_context():
            restaurants = RestaurantManager.get_restaurants_by_criteria(location='Paris')
            self.assertEqual(len(restaurants), 1)
            self.assertEqual(restaurants[0].name, 'Test Restaurant 2')

    def test_search_with_cuisine_type(self):
        with self.app.app_context():
            restaurants = RestaurantManager.get_restaurants_by_criteria(cuisine_type='Italian')
            self.assertEqual(len(restaurants), 1)
            self.assertEqual(restaurants[0].name, 'Test Restaurant 3')

    def test_search_without_criteria(self):
        with self.app.app_context():
            restaurants = RestaurantManager.get_restaurants_by_criteria()
            self.assertEqual(len(restaurants), 5)

    def test_search_with_empty_criteria(self):
        with self.app.app_context():
            restaurants = RestaurantManager.get_restaurants_by_criteria(location='', cuisine_type='')
            self.assertEqual(len(restaurants), 5)