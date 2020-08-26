import os
from application.src.db.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME', 'insurance'),
        'USER': os.getenv('DB_USER','root'),
        'PASSWORD': os.getenv('DB_PASSWORD','test'),
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


