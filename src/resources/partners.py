"""
Define the REST verbs relative to the partners
"""

from flasgger import swag_from
from flask import make_response
from flask.json import jsonify
from flask_restful import Resource, request

from models import Partner
from repositories import PartnerRepository


class PartnersResource(Resource):
    """Verbs relative to the partners"""

    not_found = {"partner": None, "message": "Partner not found."}
    should_be_json = {
        "partner": None,
        "message": "Request should include a JSON in the body.",
    }

    @staticmethod
    @swag_from("../swagger/partners/GET.yml")
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
                    "message": "The partners' data were successfully retrieved.",
                }
            ),
            200,
        )

    @staticmethod
    @swag_from("../swagger/partners/POST.yml")
    def post():
        """Create an partner based on the sent data"""
        if request.json is None:
            return make_response(jsonify(PartnersResource.should_be_json), 400)

        name = request.json["name"]
        cnpj = request.json["cnpj"]
        email = request.json["email"]
        password = request.json["password"]
        partner = PartnerRepository.create(
            name=name, cnpj=cnpj, email=email, password=password
        )
        if isinstance(partner, Partner):
            return make_response(
                jsonify(
                    {
                        "partner": partner.json,
                        "message": "Partner created successfully.",
                    }
                ),
                200,
            )

        return make_response(
            jsonify(
                {
                    "partner": None,
                    "message": partner,
                }
            ),
            400,
        )
