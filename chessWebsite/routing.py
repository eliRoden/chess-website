from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path, re_path
import logging

logger = logging.getLogger('chessWebsite')
logger.info('in routing.py')
from chessApp.consumers import ChessConsumer
logger.info('import worked')
application = ProtocolTypeRouter({
	'websocket': AllowedHostsOriginValidator(
		AuthMiddlewareStack(
			URLRouter([
                    path('ws/game/<str:game_id>/', ChessConsumer),
                ])
		)
	),
})
logger.info('passed routing')