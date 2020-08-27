from application.src.rest.insurance_policy import InsurancePolicy
from application.src.rest.ping import Ping


def setup_routes(api):
    api.add_resource(Ping, '/ping/')
    api.add_resource(InsurancePolicy, '/insurance/policy/', '/insurance/policy/<string:policy_number>/')

