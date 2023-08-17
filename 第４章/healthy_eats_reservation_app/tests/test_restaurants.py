import unittest
from flask import Flask
from src.restaurants.routes import index
from src import create_app

class RestaurantsRoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()

    def tearDown(self):
        pass

    # 正常系のテスト
    def test_home_screen_without_parameters(self):
        response = self.client.get('/restaurants/')
        self.assertEqual(response.status_code, 200)

    def test_home_screen_with_valid_parameters(self):
        response = self.client.get('/restaurants/', query_string={'location': 'Tokyo', 'cuisine_type': 'Sushi'})
        self.assertEqual(response.status_code, 200)

    # 異常系のテスト
    def test_home_screen_with_long_location(self):
        response = self.client.get('/restaurants/', query_string={'location': 'a' * 101})
        self.assertEqual(response.status_code, 400)

    def test_home_screen_with_long_cuisine_type(self):
        response = self.client.get('/restaurants/', query_string={'cuisine_type': 'a' * 51})
        self.assertEqual(response.status_code, 400)

if __name__ == "__main__":
    unittest.main()
