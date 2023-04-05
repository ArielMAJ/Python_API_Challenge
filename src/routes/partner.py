"""
Defines the blueprint for a partner
"""
from flask import Blueprint
from flask_restful import Api

from resources import PartnerResource

PARTNER_BLUEPRINT = Blueprint("partner", __name__)
Api(PARTNER_BLUEPRINT).add_resource(PartnerResource, "/partners/<int:partner_id>")
