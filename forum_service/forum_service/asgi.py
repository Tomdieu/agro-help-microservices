"""
ASGI config for forum_service project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import URLRouter, ProtocolTypeRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator

from forum.middleware import TokenAuthMiddleWare
from forum.routing import websocket_urpatterns

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "forum_service.settings")

application = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        # Just HTTP for now. (We can add other protocols later.)
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(TokenAuthMiddleWare(URLRouter(websocket_urpatterns)))
        ),
    }
)
