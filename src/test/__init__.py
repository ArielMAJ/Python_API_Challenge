"""This module contains the unit tests for the project."""

from datetime import datetime

UTC_NOW = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")

UTC_NOW_DICT = {
    "created_at": UTC_NOW,
    "updated_at": UTC_NOW,
}

PARTNER_1 = {
    "cnpj": "51660963035967",
    "email": "john@outlook.com",
    "name": "John Doe",
    "password": "12345678",
}

PARTNER_2 = {
    "cnpj": "27793841995690",
    "email": "bob@gmail.com",
    "name": "Bob Smith",
    "password": "87654321",
}


PLANT_1 = {
    "name": "Super Plant",
    "cep": "01001000",
    "latitude": 0.0,
    "longitude": 0.0,
    "max_capacity_gw": 100,
}

PLANT_2 = {
    "name": "Medium Plant",
    "cep": "01001000",
    "latitude": 1.0,
    "longitude": 1.0,
    "max_capacity_gw": 50,
}
