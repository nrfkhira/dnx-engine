from http import HTTPStatus
from flask_cors  import CORS, cross_origin
from app.core.engine import dnx
from app.model.domain import domain_model, domain_reqparser
from flask_restx import Namespace, Resource

domain_ns = Namespace(name="domain", validate=True)
domain_ns.models[domain_model.name] = domain_model
# CORS(domain_ns)

@domain_ns.route("/query", endpoint="domain_query")
# @cross_origin(origin="*")
class DomainQuery(Resource):
    """Handles HTTP requests to URL: /api/v1/domain/query."""

    @domain_ns.expect(domain_reqparser)
    @domain_ns.response(int(HTTPStatus.OK), "Query succeeded.")
    @domain_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
    @domain_ns.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
    def get(self):
        """Query single domain and return result in JSON."""
        request_data = domain_reqparser.parse_args()
        domain = request_data.get("domain")
        return dnx(domain)
