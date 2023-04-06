"""
Define the REST verbs relative to a plant
"""
from datetime import datetime

from flask import make_response
from flask.json import jsonify
from flask_restful import Resource, request

from models import Plant
from repositories import PlantRepository


class PlantResource(Resource):
    """Verbs relative to the plant"""

    should_be_json = {
        "plant": None,
        "message": "Request should include a JSON in the body.",
    }

    @staticmethod
    def get(plant_id):
        """Return an plant key information based on id"""
        plant = PlantRepository.get(plant_id)
        if isinstance(plant, Plant):
            return make_response(
                jsonify(
                    {
                        "plant": plant.json,
                        "message": "The plant's information were successfully retrieved.",
                    }
                ),
                200,
            )

        return PlantResource.error(None, plant, 404)

    @staticmethod
    def put(plant_id):
        """Update an plant based on the sent information"""
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
    def delete(plant_id):
        """Delete a plant's information based on id"""
        plant = PlantRepository.delete(plant_id)
        if isinstance(plant, Plant):
            return make_response(
                jsonify(
                    {
                        "plant": plant.json,
                        "message": "The plant's information were successfully deleted.",
                    }
                ),
                200,
            )

        return PlantResource.error(None, plant, 404)

    @staticmethod
    def error(obj, message, code):
        """Return an error message"""
        return make_response(jsonify({"plant": obj, "message": message}), code)
