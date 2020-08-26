from application.src.common.base_resource import BaseResource
from flask import current_app as app

class Ping(BaseResource):
    def get(self):
        app.logger.info("Ping successful")
        return {"success": True}
