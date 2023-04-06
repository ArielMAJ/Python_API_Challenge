"""
Define the Plant model
"""
from datetime import datetime

from .abc import BaseModel
from .db import db


class Plant(db.Model, BaseModel):
    """The Plant model"""

    __tablename__ = "plant"

    plant_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        unique=True,
        index=True,
    )

    name = db.Column(db.String(300), nullable=False)
    cep = db.Column(db.String(8), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    max_capacity_gw = db.Column(db.Integer, nullable=False)
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow,
    )
    updated_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow,
    )

    def __init__(self, name, cep, latitude, longitude, max_capacity_gw):
        """Create a new Plant"""
        self.name = name
        self.cep = cep
        self.latitude = latitude
        self.longitude = longitude
        self.max_capacity_gw = max_capacity_gw

        default_time = datetime.utcnow()
        self.created_at = default_time
        self.updated_at = default_time
