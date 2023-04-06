"""
Define the Partner model
"""
from datetime import datetime

from werkzeug.security import check_password_hash, generate_password_hash

from .abc import BaseModel
from .db import db


class Partner(db.Model, BaseModel):
    """The Partner model"""

    __tablename__ = "partner"

    partner_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        unique=True,
        index=True,
    )
    name = db.Column(db.String(300), nullable=False)
    cnpj = db.Column(db.String(14), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
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

    def __init__(self, name, cnpj, email, password):
        """Create a new Partner"""
        self.name = name
        self.cnpj = cnpj
        self.email = email.lower()
        self.password = generate_password_hash(password)

        default_time = datetime.utcnow()
        self.created_at = default_time
        self.updated_at = default_time

    def set_password(self, password):
        """Create a hashed password."""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)
