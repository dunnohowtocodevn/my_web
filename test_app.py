import unittest
from app import app

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_addition(self):
        response = self.app.post('/', data=dict(a='2', b='3', operation='add'))
        self.assertIn(b'Result: 5.0', response.data)

    def test_subtraction(self):
        response = self.app.post('/', data=dict(a='5', b='3', operation='subtract'))
        self.assertIn(b'Result: 2.0', response.data)

    def test_multiplication(self):
        response = self.app.post('/', data=dict(a='4', b='3', operation='multiply'))
        self.assertIn(b'Result: 12.0', response.data)

    def test_division(self):
        response = self.app.post('/', data=dict(a='6', b='3', operation='divide'))
        self.assertIn(b'Result: 2.0', response.data)

    def test_division_by_zero(self):
        response = self.app.post('/', data=dict(a='6', b='0', operation='divide'))
        self.assertIn(b'Error: Division by zero', response.data)

if __name__ == '__main__':
    unittest.main()