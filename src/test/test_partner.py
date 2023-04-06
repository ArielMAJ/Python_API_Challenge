"""Test `partner` endpoints"""

import json
import unittest
from time import sleep

from werkzeug.security import check_password_hash

import config
from models import Partner, db
from repositories import PartnerRepository
from server import create_app

from . import PARTNER_1, PARTNER_2


class TestPartner(unittest.TestCase):
    """Test `partner` endpoints"""

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
        """GET on `/partners/<int:partner_id>` should return a partner"""
        partner_1 = PartnerRepository.create(**PARTNER_1)
        self.assertIsNotNone(partner_1)
        self.assertIsInstance(partner_1, Partner)

        response = self.client.get("/partners/1")
        self.assertIsNotNone(response)

        self.assertEqual(response.status_code, 200)

        response_json = json.loads(response.data.decode("utf-8"))
        self.assertIsNotNone(response_json)

        self.assertTrue(
            check_password_hash(
                response_json["partner"]["password"],
                PARTNER_1["password"],
            )
        )

        self.assertEqual(
            response_json,
            {
                "message": "The partner's information were successfully retrieved.",
                "partner": partner_1.json,
            },
        )

    def test_update(self):
        """PUT on `/partners/<int:partner_id>` should update the partner with
        partner_id=<partner_id>."""
        partner_0 = PartnerRepository.create(**PARTNER_1)
        self.assertIsNotNone(partner_0)
        self.assertIsInstance(partner_0, Partner)
        self.assertEqual(partner_0.created_at, partner_0.updated_at)

        sleep(0.1)
        response = self.client.put(
            "/partners/1",
            content_type="application/json",
            data=json.dumps(PARTNER_2),
        )

        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.data.decode("utf-8"))
        partner = PartnerRepository.get(1)
        self.assertIsInstance(partner, Partner)

        self.assertEqual(
            response_json,
            {
                "message": "The partner was successfully updated.",
                "partner": partner.json,
            },
        )
        self.assertEqual(Partner.query.count(), 1)
        self.assertEqual(partner.name, PARTNER_2["name"])
        self.assertEqual(partner.email, PARTNER_2["email"])
        self.assertEqual(partner.cnpj, PARTNER_2["cnpj"])
        self.assertTrue(
            check_password_hash(
                partner.password,
                PARTNER_2["password"],
            )
        )
        self.assertNotEqual(partner.created_at, partner.updated_at)

    def test_delete(self):
        """DELETE on `/partners/<int:partner_id>` should delete the partner
        with partner_id=<partner_id>"""
        response = self.client.delete("/partners/1")

        self.assertEqual(response.status_code, 404)

        response_json = json.loads(response.data.decode("utf-8"))
        self.assertEqual(
            response_json,
            {"partner": None, "message": "Partner not found."},
        )
        self.assertEqual(Partner.query.count(), 0)

        partner1 = PartnerRepository.create(**PARTNER_1)
        self.assertIsInstance(partner1, Partner)
        self.assertEqual(Partner.query.count(), 1)

        partner2 = PartnerRepository.create(**PARTNER_2)
        self.assertIsInstance(partner2, Partner)
        self.assertEqual(Partner.query.count(), 2)

        response = self.client.delete("/partners/1")

        response_json = json.loads(response.data.decode("utf-8"))
        self.assertEqual(
            response_json,
            {
                "partner": partner1.json,
                "message": "The partner's information were successfully deleted.",
            },
        )
        self.assertEqual(Partner.query.count(), 1)

        response = self.client.delete("/partners/1")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(Partner.query.count(), 1)

        response = self.client.delete("/partners/2")
        response_json = json.loads(response.data.decode("utf-8"))
        self.assertEqual(
            response_json,
            {
                "partner": partner2.json,
                "message": "The partner's information were successfully deleted.",
            },
        )
        self.assertEqual(Partner.query.count(), 0)

        response = self.client.delete("/partners/2")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(Partner.query.count(), 0)
