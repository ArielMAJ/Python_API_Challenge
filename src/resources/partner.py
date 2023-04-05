"""
Define the REST verbs relative to a partner
"""
from datetime import datetime

from flask import make_response
from flask.json import jsonify
from flask_restful import Resource, request

from models import Partner
from repositories import PartnerRepository


class PartnerResource(Resource):
    """Verbs relative to the partner"""

    should_be_json = {
        "partner": None,
        "message": "Request should include a JSON in the body.",
    }

    @staticmethod
    def get(partner_id):
        """Return an partner key information based on id"""
        partner = PartnerRepository.get(partner_id)
        if isinstance(partner, Partner):
            return make_response(
                jsonify(
                    {
                        "partner": partner.json,
                        "message": "The partner's information were successfully retrieved.",
                    }
                ),
                200,
            )

        return PartnerResource.error(None, partner, 404)

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
        updated_at = datetime.utcnow()
        partner = repository.update(
            partner_id=partner_id,
            name=name,
            cnpj=cnpj,
            email=email,
            password=password,
            updated_at=updated_at,
        )

        if isinstance(partner, Partner):
            return make_response(
                jsonify(
                    {
                        "partner": partner.json,
                        "message": "The partner was successfully updated.",
                    }
                ),
                200,
            )
        return PartnerResource.error(None, partner, 404)

    @staticmethod
    def delete(partner_id):
        """Delete a partner's information based on id"""
        partner = PartnerRepository.delete(partner_id)
        if isinstance(partner, Partner):
            return make_response(
                jsonify(
                    {
                        "partner": partner.json,
                        "message": "The partner's information were successfully deleted.",
                    }
                ),
                200,
            )

        return PartnerResource.error(None, partner, 404)

    @staticmethod
    def error(obj, message, code):
        """Return an error message"""
        return make_response(jsonify({"partner": obj, "message": message}), code)
