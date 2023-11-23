import unittest

from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_hello_world(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Hello, World!")


if __name__ == "__main__":
    unittest.main()
