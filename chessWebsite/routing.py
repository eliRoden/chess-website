from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from django.urls import path, re_path
import logging

django_asgi_app = get_asgi_application
logger = logging.getLogger('chessWebsite')
logger.info('in routing.py')
from chessApp import consumers
logger.info('import worked')
application = ProtocolTypeRouter({
    'http': django_asgi_app,
	'websocket': AllowedHostsOriginValidator(
		AuthMiddlewareStack(
			URLRouter([
                    re_path(r"ws/game/(?P<game_id>\w+)/$", consumers.ChessConsumer.as_asgi()),

                ])
		)
	),
})
logger.info('passed routing')