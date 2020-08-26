import importlib
import os

from application.src.config.environments.constants import  STAGING, DEVELOPMENT, ENVIRONMENT

CONFIG_MAP = {
    'development': DEVELOPMENT,
    'staging': STAGING
}


def get_configurations(env):
    return '.'.join(['application','src', 'config', 'environments', CONFIG_MAP.get(env, env), 'Config'])


def get_env_config():
    env = os.environ.get(ENVIRONMENT, DEVELOPMENT)
    config = get_configurations(env).replace('.Config', '')
    config_module = importlib.import_module(config)
    return config_module.Config
