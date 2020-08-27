from flask.globals import request
from flask import current_app as app

from application.src.common.base_resource import BaseResource
from application.src.common.exceptions.error_handler import ErrorHandler
from application.src.common.response_utils import ok_response
from application.src.controller.insurance_policy_access import create_insurance_policy, get_insurance_policy
from flask_csv import send_csv


class InsurancePolicy(BaseResource):
    @ErrorHandler("Insurance Get API", app)
    def get(self, policy_number=None):
        app.logger.info("Received get insurance policy")
        params = request.args.to_dict()
        response = get_insurance_policy(params, policy_number)
        format = params.get("format", "json")
        if format == "csv":
            if type(response) == dict:
                response = [response]
            return send_csv(response, "insurance_policies.csv",
                            ["userId", "policyNumber", "nameOfInsured", "type", "startDate", "amountInsured",
                             "expirationDate"])
        return ok_response(response)

    @ErrorHandler("Insurance Post API", app)
    def post(self):
        request_data = request.get_json(force=True)
        app.logger.info("Received create insurance request")
        response = create_insurance_policy(request_data)
        return ok_response(response)
