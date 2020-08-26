from application.src.rest.ping import Ping


def setup_routes(api):
    api.add_resource(Ping, '/ping/')
