"""Test the swagger spec"""

import json
import unittest
import warnings

import config
from server import create_app


class TestSwagger(unittest.TestCase):
    """Test the swagger spec"""

    @classmethod
    def setUpClass(cls):
        server = create_app(config.TestConfig)
        cls.client = server.test_client()

    def test_get_spec(self):
        """The GET on /spec should return a 200"""

        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", message="unclosed file")
            response = self.client.get("/application/spec")
        self.assertEqual(response.status_code, 200)

    def test_swagger_is_not_empty(self):
        """
        The GET on /spec should return a dict with a non-empty paths property
        """

        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", message="unclosed file")
            response = self.client.get("/application/spec")
        response_json = json.loads(response.data.decode("utf-8"))
        self.assertTrue(response_json["paths"])
