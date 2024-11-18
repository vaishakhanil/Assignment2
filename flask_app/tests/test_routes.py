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

        # Expect 405 Method Not Allowed when trying to send post request for '/'
        self.assertEqual(response.status_code, 405)  

    # Test if the /products route works with GET
    def test_products_route_get(self):
        # Send a GET request to the /products route
        response = self.app.get('/products')

        # Expect 200 OK
        self.assertEqual(response.status_code, 200)  

        # Check if the page contains the word "Our Products" - The title
        self.assertIn(b"Our Products", response.data)  

if __name__ == "__main__":
    unittest.main()
