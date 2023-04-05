"""
Define the REST verbs relative to the partners
"""

from flask import make_response
from flask.json import jsonify
from flask_restful import Resource, request

from repositories import PartnerRepository


class PartnerResource(Resource):
    """Verbs relative to the partner"""

    not_found = {"partner": None, "message": "Partner not found."}
    should_be_json = {
        "partner": None,
        "message": "Request should include a JSON in the body.",
    }

    @staticmethod
    def get(partner_id):
        """Return an partner key information based on id"""
        partner = PartnerRepository.get(partner_id)
        if partner is not None:
            return jsonify(
                {
                    "partner": partner.json,
                    "message": "The partner's information were successfully retrieved.",
                }
            )

        return make_response(jsonify(PartnerResource.not_found), 404)

    @staticmethod
    def put(partner_id):
        """Update an partner based on the sent information"""
        repository = PartnerRepository()
        if request.json is None:
            return make_response(jsonify(PartnerResource.should_be_json), 400)

        name = request.json["name"]
        cnpj = request.json["cnpj"]
        email = request.json["email"]
        password = request.json["password"]
        partner = repository.update(
            partner_id=partner_id, name=name, cnpj=cnpj, email=email, password=password
        )

        if partner is not None:
            return jsonify(
                {
                    "partner": partner.json,
                    "message": "The partner was successfully updated.",
                }
            )
        return make_response(jsonify(PartnerResource.not_found), 404)
