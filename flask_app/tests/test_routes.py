import unittest
from app import app

class FlaskRouteTest(unittest.TestCase):
    # Set up the Flask test client
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Test for invalid method (POST instead of GET)
    def test_home_route_invalid_method(self):
        # Send a POST request to the home route
        response = self.app.post('/')
        self.assertEqual(response.status_code, 405)  # Expect 405 Method Not Allowed

    # Test if the /products route works with GET
    def test_products_route_get(self):
        # Send a GET request to the /products route
        response = self.app.get('/products')
        self.assertEqual(response.status_code, 200)  # Expect 200 OK
        self.assertIn(b"Our Products", response.data)  # Check if the page contains the word "Products"

if __name__ == "__main__":
    unittest.main()
