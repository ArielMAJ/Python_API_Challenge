"""
Defines the blueprint for the plants
"""
from flask import Blueprint
from flask_restful import Api

from resources import PlantsResource

PLANTS_BLUEPRINT = Blueprint("plants", __name__)
Api(PLANTS_BLUEPRINT).add_resource(PlantsResource, "/plants/")
