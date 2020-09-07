import logging
import os

from application.src.config.environments import get_configurations
from application.src.config.environments.constants import DEVELOPMENT, ENVIRONMENT
from application.src.dao.inmemory_insurance_policy import InMemoryInsurancePolicy
from application.src.utils.date_time import timestamp_to_datetime

log_format = ' '.join([
    '[%(asctime)s]',
    '[%(process)d-%(thread)d]',
    '%(levelname)s',
    '-',
    '%(message)s'
])

formatter = logging.Formatter(log_format)


def setup_test_data():
    InMemoryInsurancePolicy.create_new_insurance_policy(1, "6316-14738430-02-0010", "Kasim Sharif", "MOTOR",
                                                        timestamp_to_datetime(1609326432000),
                                                        timestamp_to_datetime(1640862432000), 10000)
    InMemoryInsurancePolicy.create_new_insurance_policy(2, "6316-14738430-02-0011", "Hasan Sharif", "HEALTH",
                                                        timestamp_to_datetime(1609326432000),
                                                        timestamp_to_datetime(1640862432000), 100000)
    InMemoryInsurancePolicy.create_new_insurance_policy(3, "6316-14738430-02-0012", "Sanket Patil", "TRAVEL",
                                                        timestamp_to_datetime(1609326432000),
                                                        timestamp_to_datetime(1640862432000), 100000)


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
    app.logger.info("Initializing the test data")
    setup_test_data()
    app.logger.info("test data initialize")
