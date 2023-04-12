"""
Defines the blueprint for plant.
"""
from flask import Blueprint
from flask_restful import Api

from resources import PlantResource

PLANT_BLUEPRINT = Blueprint("plant", __name__)
Api(PLANT_BLUEPRINT).add_resource(PlantResource, "/plants/<int:plant_id>")
