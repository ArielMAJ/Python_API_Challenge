"""Test `plants` endpoints"""

import json
import unittest

import config
from models import Plant, db
from repositories import PlantRepository
from server import create_app

from . import PLANT_1, PLANT_2, UTC_NOW_DICT


class TestPlant(unittest.TestCase):
    """Test `plants` endpoints"""

    @classmethod
    def setUpClass(cls):
        cls.server = create_app(config.TestConfig)
        cls.client = cls.server.test_client()

    def setUp(self):
        self.app_context = self.server.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_get(self):
        """GET on `/plants/` should return all plants"""
        plant_1 = PlantRepository.create(**PLANT_1)
        plant_2 = PlantRepository.create(**PLANT_2)
        self.assertIsNotNone(plant_1)
        self.assertIsNotNone(plant_2)
        self.assertIsInstance(plant_1, Plant)
        self.assertIsInstance(plant_2, Plant)

        response = self.client.get("/plants/")
        self.assertIsNotNone(response)

        self.assertEqual(response.status_code, 200)

        response_json = json.loads(response.data.decode("utf-8"))
        self.assertIsNotNone(response_json)

        self.assertEqual(
            response_json,
            {
                "message": "The plants' data were successfully retrieved.",
                "plants": [plant_1.json, plant_2.json],
            },
        )

    def test_get_top_capacity_plants(self):
        """GET on `/plants/?top=value` should return top `value` capacity plants"""

        self.assertEqual(Plant.query.count(), 0)
        plant_1 = PlantRepository.create(**PLANT_1)
        self.assertEqual(Plant.query.count(), 1)
        plant_2 = PlantRepository.create(**PLANT_2)
        self.assertEqual(Plant.query.count(), 2)
        self.assertIsNotNone(plant_1)
        self.assertIsNotNone(plant_2)
        self.assertIsInstance(plant_1, Plant)
        self.assertIsInstance(plant_2, Plant)

        response = self.client.get("/plants/?last=1")
        self.assertIsNotNone(response)

        self.assertEqual(response.status_code, 200)

        response_json = json.loads(response.data.decode("utf-8"))
        self.assertIsNotNone(response_json)

        self.assertDictEqual(
            response_json,
            {
                "message": "The plants' data were successfully retrieved.",
                "plants": [plant_1.json, plant_2.json],
            },
        )
        self.assertEqual(Plant.query.count(), 2)

        self.assertEqual(plant_1.name, response_json["plants"][0]["name"])
        self.assertEqual(plant_1.cep, response_json["plants"][0]["cep"])
        self.assertEqual(
            plant_1.latitude, response_json["plants"][0]["latitude"]
        )
        self.assertEqual(
            plant_1.longitude, response_json["plants"][0]["longitude"]
        )
        self.assertEqual(
            plant_1.max_capacity_gw,
            response_json["plants"][0]["max_capacity_gw"],
        )

    def test_create(self):
        """POST on `/plants/` should create a plant"""
        response = self.client.post(
            "/plants/",
            content_type="application/json",
            data=json.dumps(PLANT_1),
        )
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.data.decode("utf-8"))
        self.assertIsNotNone(response_json)

        plant_1 = PLANT_1.copy()
        plant_1.update(plant_id=1, **UTC_NOW_DICT)
        response_json["plant"].update(**UTC_NOW_DICT)

        self.assertEqual(
            response_json,
            {
                "plant": plant_1,
                "message": "Plant created successfully.",
            },
        )
        self.assertEqual(Plant.query.count(), 1)
