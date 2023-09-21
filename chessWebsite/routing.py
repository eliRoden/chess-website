from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path, re_path

from chessApp.consumers import ChessConsumer

application = ProtocolTypeRouter({
    "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(
                URLRouter([
                    re_path(r"ws/game/(?P<game_id>\w+)/$", ChessConsumer.as_asgi()),
                ])
            )
        ),
})