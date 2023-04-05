"""
Define the REST verbs relative to the partners
"""

from flask import make_response
from flask.json import jsonify
from flask_restful import Resource, request

from repositories import PartnerRepository


class PartnersResource(Resource):
    """Verbs relative to the partners"""

    not_found = {"partner": None, "message": "Partner not found."}
    should_be_json = {
        "partner": None,
        "message": "Request should include a JSON in the body.",
    }

    @staticmethod
    def get():
        """If argument "last=value" is sent, return the last "value" partners.
        Else return all partners"""
        args = request.args
        if args is not None and "last" in args:
            last = int(args["last"])
            partners = PartnerRepository.get_last(last)
        else:
            partners = PartnerRepository.get_all()

        return make_response(
            jsonify(
                {
                    "partners": [partner.json for partner in partners],
                    "message": "The partners' information were successfully retrieved.",
                }
            ),
            200,
        )

    @staticmethod
    def post():
        """Create an partner based on the sent information"""
        if request.json is None:
            return make_response(jsonify(PartnersResource.should_be_json), 400)

        name = request.json["name"]
        cnpj = request.json["cnpj"]
        email = request.json["email"]
        password = request.json["password"]
        partner = PartnerRepository.create(
            name=name, cnpj=cnpj, email=email, password=password
        )
        if partner is not None:
            return jsonify(
                {"partner": partner.json, "message": "Partner created successfully."}
            )

        return make_response(
            jsonify(
                {
                    "partner": None,
                    "message": "Partner CNPJ or email already exists.",
                }
            ),
            409,
        )
