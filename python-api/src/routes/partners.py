"""
Defines the blueprint for partners.
"""
from flask import Blueprint
from flask_restful import Api

from resources import PartnersResource

PARTNERS_BLUEPRINT = Blueprint("partners", __name__)
Api(PARTNERS_BLUEPRINT).add_resource(PartnersResource, "/partners/")
