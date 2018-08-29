from .base import *

ALLOWED_HOSTS=['*']
INSTALLED_APPS += ['channels']
ASGI_APPLICATION = 'spkchat.routing.application'
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("localhost", 6379)],
        },
        "symmetric_encryption_keys": [SECRET_KEY],
    },
}
