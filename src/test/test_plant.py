"""Test `plant` endpoints"""

import json
import unittest
from time import sleep

import config
from models import Plant, db
from repositories import PlantRepository
from server import create_app

from . import PLANT_1, PLANT_2


class TestPlant(unittest.TestCase):
    """Test `plant` endpoints"""

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
        """GET on `/plants/<int:plant_id>` should return a plant"""
        plant_1 = PlantRepository.create(**PLANT_1)
        self.assertIsNotNone(plant_1)
        self.assertIsInstance(plant_1, Plant)

        response = self.client.get("/plants/1")
        self.assertIsNotNone(response)

        self.assertEqual(response.status_code, 200)

        response_json = json.loads(response.data.decode("utf-8"))
        self.assertIsNotNone(response_json)

        self.assertEqual(
            response_json,
            {
                "message": "The plant's information were successfully retrieved.",
                "plant": plant_1.json,
            },
        )

    def test_update(self):
        """PUT on `/plants/<int:plant_id>` should update a plant."""
        plant_0 = PlantRepository.create(**PLANT_1)
        self.assertIsNotNone(plant_0)
        self.assertIsInstance(plant_0, Plant)
        self.assertEqual(plant_0.created_at, plant_0.updated_at)

        sleep(0.1)
        response = self.client.put(
            "/plants/1",
            content_type="application/json",
            data=json.dumps(PLANT_2),
        )

        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.data.decode("utf-8"))
        plant = PlantRepository.get(1)
        self.assertIsInstance(plant, Plant)

        self.assertEqual(
            response_json,
            {
                "message": "The plant was successfully updated.",
                "plant": plant.json,
            },
        )
        self.assertEqual(Plant.query.count(), 1)
        self.assertEqual(plant.name, PLANT_2["name"])
        self.assertEqual(plant.cep, PLANT_2["cep"])
        self.assertEqual(plant.latitude, PLANT_2["latitude"])
        self.assertEqual(plant.longitude, PLANT_2["longitude"])
        self.assertEqual(plant.max_capacity_gw, PLANT_2["max_capacity_gw"])
        self.assertNotEqual(plant.created_at, plant.updated_at)

    def test_delete(self):
        """DELETE on `/plants/<int:plant_id>` should delete a plant"""
        response = self.client.delete("/plants/1")

        self.assertEqual(response.status_code, 404)

        response_json = json.loads(response.data.decode("utf-8"))
        self.assertEqual(
            response_json,
            {"plant": None, "message": "Plant not found."},
        )
        self.assertEqual(Plant.query.count(), 0)

        plant1 = PlantRepository.create(**PLANT_1)
        self.assertIsInstance(plant1, Plant)
        self.assertEqual(Plant.query.count(), 1)

        plant2 = PlantRepository.create(**PLANT_2)
        self.assertIsInstance(plant2, Plant)
        self.assertEqual(Plant.query.count(), 2)

        response = self.client.delete("/plants/1")

        response_json = json.loads(response.data.decode("utf-8"))
        self.assertEqual(
            response_json,
            {
                "plant": plant1.json,
                "message": "The plant's information were successfully deleted.",
            },
        )
        self.assertEqual(Plant.query.count(), 1)

        response = self.client.delete("/plants/1")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(Plant.query.count(), 1)

        response = self.client.delete("/plants/2")
        response_json = json.loads(response.data.decode("utf-8"))
        self.assertEqual(
            response_json,
            {
                "plant": plant2.json,
                "message": "The plant's information were successfully deleted.",
            },
        )
        self.assertEqual(Plant.query.count(), 0)

        response = self.client.delete("/plants/2")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(Plant.query.count(), 0)
