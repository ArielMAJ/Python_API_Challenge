"""Test `partners` endpoints"""

import json
import unittest

from werkzeug.security import check_password_hash

import config
from models import Partner, db
from repositories import PartnerRepository
from server import create_app

from . import PARTNER_1, PARTNER_2, UTC_NOW_DICT


class TestPartner(unittest.TestCase):
    """Test `partners` endpoints"""

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
        """GET on `/partners/` should return all partners"""
        partner_1 = PartnerRepository.create(**PARTNER_1)
        partner_2 = PartnerRepository.create(**PARTNER_2)
        self.assertIsNotNone(partner_1)
        self.assertIsNotNone(partner_2)
        self.assertIsInstance(partner_1, Partner)
        self.assertIsInstance(partner_2, Partner)

        response = self.client.get("/partners/")
        self.assertIsNotNone(response)

        self.assertEqual(response.status_code, 200)

        response_json = json.loads(response.data.decode("utf-8"))
        self.assertIsNotNone(response_json)

        self.assertTrue(
            check_password_hash(
                response_json["partners"][0]["password"], PARTNER_1["password"]
            )
        )
        self.assertTrue(
            check_password_hash(
                response_json["partners"][1]["password"], PARTNER_2["password"]
            )
        )

        self.assertEqual(
            response_json,
            {
                "message": "The partners' information were successfully retrieved.",
                "partners": [partner_1.json, partner_2.json],
            },
        )

    def test_get_last(self):
        """GET on `/partners/?last=value` should return last `value` partners
        added, by creation date"""

        self.assertEqual(Partner.query.count(), 0)
        partner_1 = PartnerRepository.create(**PARTNER_1)
        self.assertEqual(Partner.query.count(), 1)
        partner_2 = PartnerRepository.create(**PARTNER_2)
        self.assertEqual(Partner.query.count(), 2)
        self.assertIsNotNone(partner_1)
        self.assertIsNotNone(partner_2)
        self.assertIsInstance(partner_1, Partner)
        self.assertIsInstance(partner_2, Partner)

        response = self.client.get("/partners/?last=1")
        self.assertIsNotNone(response)

        self.assertEqual(response.status_code, 200)

        response_json = json.loads(response.data.decode("utf-8"))
        self.assertIsNotNone(response_json)

        self.assertTrue(
            check_password_hash(
                response_json["partners"][0]["password"], PARTNER_2["password"]
            )
        )

        self.assertEqual(
            response_json,
            {
                "message": "The partners' information were successfully retrieved.",
                "partners": [partner_2.json],
            },
        )
        self.assertEqual(Partner.query.count(), 2)
        self.assertEqual(partner_2.name, response_json["partners"][0]["name"])
        self.assertEqual(
            partner_2.email, response_json["partners"][0]["email"]
        )
        self.assertEqual(partner_2.cnpj, response_json["partners"][0]["cnpj"])
        self.assertEqual(
            partner_2.password, response_json["partners"][0]["password"]
        )

    def test_create(self):
        """POST on `/partners/` should create a partner"""
        response = self.client.post(
            "/partners/",
            content_type="application/json",
            data=json.dumps(PARTNER_1),
        )
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.data.decode("utf-8"))
        self.assertIsNotNone(response_json)

        self.assertTrue(
            check_password_hash(
                response_json["partner"]["password"], PARTNER_1["password"]
            )
        )

        partner_1 = PARTNER_1.copy()
        partner_1.update(partner_id=1, **UTC_NOW_DICT)
        partner_1["password"] = response_json["partner"]["password"]
        response_json["partner"].update(**UTC_NOW_DICT)

        self.assertEqual(
            response_json,
            {
                "partner": partner_1,
                "message": "Partner created successfully.",
            },
        )
        self.assertEqual(Partner.query.count(), 1)
