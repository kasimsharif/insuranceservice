import django
django.setup()

from application.src.rest.insurance_policy import InsurancePolicy
from application.src.rest.ping import Ping
from os.path import dirname, abspath

from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from application.src.config.setup import setup_app

app = Flask(__name__)
CORS(app)

app.root_dir = dirname(dirname(abspath(__file__)))
api = Api(app)
api.add_resource(Ping, '/ping/')
api.add_resource(InsurancePolicy, '/insurance/policy/', '/insurance/policy/<string:policy_number>/')
setup_app(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=7500)
