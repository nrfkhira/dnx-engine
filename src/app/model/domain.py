"""Parsers and serializers for /domain API endpoints."""
from flask_restx import Model
from flask_restx.fields import String
from flask_restx.reqparse import RequestParser


domain_reqparser = RequestParser(bundle_errors=True)
domain_reqparser.add_argument(
    name="domain", type=str, location="args", required=True, nullable=False
)

domain_model = Model(
    "Domain",
    {
        "email": String,
        "public_id": String,
        "registered_on": String(attribute="registered_on_str"),
        "token_expires_in": String,
    },
)