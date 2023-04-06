"""
Define the REST verbs relative to a plant
"""
from datetime import datetime

from flask import make_response
from flask.json import jsonify
from flask_restful import Resource, request
from flasgger import swag_from

from models import Plant
from repositories import PlantRepository


class PlantResource(Resource):
    """Verbs relative to the plant"""

    should_be_json = {
        "plant": None,
        "message": "Request should include a JSON in the body.",
    }

    @staticmethod
    @swag_from("../swagger/plant/GET.yml")
    def get(plant_id):
        """Return an plant key data based on id"""
        plant = PlantRepository.get(plant_id)
        if isinstance(plant, Plant):
            return make_response(
                jsonify(
                    {
                        "plant": plant.json,
                        "message": "The plant's data were successfully retrieved.",
                    }
                ),
                200,
            )

        return PlantResource.error(None, plant, 404)

    @staticmethod
    @swag_from("../swagger/plant/PUT.yml")
    def put(plant_id):
        """Update an plant based on the sent data"""
        repository = PlantRepository()
        if request.json is None:
            return make_response(jsonify(PlantResource.should_be_json), 400)

        name = request.json["name"]
        cep = request.json["cep"]
        latitude = request.json["latitude"]
        longitude = request.json["longitude"]
        max_capacity_gw = request.json["max_capacity_gw"]
        updated_at = datetime.utcnow()

        plant = repository.update(
            plant_id=plant_id,
            name=name,
            cep=cep,
            latitude=latitude,
            longitude=longitude,
            max_capacity_gw=max_capacity_gw,
            updated_at=updated_at,
        )

        if isinstance(plant, Plant):
            return make_response(
                jsonify(
                    {
                        "plant": plant.json,
                        "message": "The plant was successfully updated.",
                    }
                ),
                200,
            )
        return PlantResource.error(None, plant, 404)

    @staticmethod
    @swag_from("../swagger/plant/DELETE.yml")
    def delete(plant_id):
        """Delete a plant's data based on id"""
        plant = PlantRepository.delete(plant_id)
        if isinstance(plant, Plant):
            return make_response(
                jsonify(
                    {
                        "plant": plant.json,
                        "message": "The plant's data were successfully deleted.",
                    }
                ),
                200,
            )

        return PlantResource.error(None, plant, 404)

    @staticmethod
    def error(obj, message, code):
        """Return an error message"""
        return make_response(jsonify({"plant": obj, "message": message}), code)
