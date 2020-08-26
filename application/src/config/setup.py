import logging
import os

from application.src.config.environments import get_configurations
from application.src.config.environments.constants import DEVELOPMENT, ENVIRONMENT

log_format = ' '.join([
    '[%(asctime)s]',
    '[%(process)d-%(thread)d]',
    '%(levelname)s',
    '-',
    '%(message)s'
])

formatter = logging.Formatter(log_format)


def setup_app(app):
    app.secret_key = "11ca4c58-90ab-46c6-bf1c-d26e630f0d74"
    env = os.environ.get(ENVIRONMENT, DEVELOPMENT)
    config = get_configurations(env)
    app.config.from_object(config)
    app.debug_log_format = log_format

    if not app.debug:
        logHandler = logging.StreamHandler()

    logHandler.setFormatter(formatter)
    logHandler.setLevel(logging.DEBUG)
    app.logger.addHandler(logHandler)
    app.logger.setLevel(logging.DEBUG)

    app.logger.info("Loaded environment: " + env)
