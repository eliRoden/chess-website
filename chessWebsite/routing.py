from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path, re_path

from chessApp.consumers import ChessConsumer
print('in asgi.py')

application = ProtocolTypeRouter({
    "websocket": AllowedHostsOriginValidator(
                URLRouter([
                    path('game/<str:game_id>/', ChessConsumer),
                ])
        ),
})