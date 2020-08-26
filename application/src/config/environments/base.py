class BaseConfig(object):
    CORS_ALLOW_HEADERS = ['Origin', 'X-Requested-With', 'Content-Type',
                          'Accept']
    CORS_ALLOW_ORIGIN = ['*']