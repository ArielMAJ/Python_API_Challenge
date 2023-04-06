"""
Define the REST verbs relative to the plants
"""

from flask import make_response
from flask.json import jsonify
from flask_restful import Resource, request

from models import Plant
from repositories import PlantRepository


class PlantsResource(Resource):
    """Verbs relative to the plants"""

    not_found = {"plant": None, "message": "Plant not found."}
    should_be_json = {
        "plant": None,
        "message": "Request should include a JSON in the body.",
    }

    @staticmethod
    def get():
        """If argument "top=value" is sent, return the top "value" plants.
        Else return all plants"""
        args = request.args
        if args is not None and "top" in args:
            top = int(args["top"])
            plants = PlantRepository.get_top_capacity_plants(top)
        else:
            plants = PlantRepository.get_all()

        return make_response(
            jsonify(
                {
                    "plants": [plant.json for plant in plants],
                    "message": "The plants' information were successfully retrieved.",
                }
            ),
            200,
        )

    @staticmethod
    def post():
        """Create an plant based on the sent information"""
        if request.json is None:
            return make_response(jsonify(PlantsResource.should_be_json), 400)

        name = request.json["name"]
        cep = request.json["cep"]
        latitude = request.json["latitude"]
        longitude = request.json["longitude"]
        max_capacity_gw = request.json["max_capacity_gw"]

        plant = PlantRepository.create(
            name=name,
            cep=cep,
            latitude=latitude,
            longitude=longitude,
            max_capacity_gw=max_capacity_gw,
        )
        if isinstance(plant, Plant):
            return make_response(
                jsonify(
                    {
                        "plant": plant.json,
                        "message": "Plant created successfully.",
                    }
                ),
                200,
            )

        return make_response(
            jsonify(
                {
                    "plant": None,
                    "message": plant,
                }
            ),
            409,
        )
