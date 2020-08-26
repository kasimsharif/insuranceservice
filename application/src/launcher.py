import django
django.setup()
from os.path import dirname, abspath

from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from application.src.config.setup import setup_app
from application.src.routes import setup_routes

app = Flask(__name__)
CORS(app)

app.root_dir = dirname(dirname(abspath(__file__)))
api = Api(app)
setup_routes(api)
setup_app(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=7500)
