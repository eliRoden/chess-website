import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
import logging 

logger = logging.getLogger('chessApp')

class ChessConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        logger.info('in consumer connect')
        self.game_id = self.scope["url_route"]["kwargs"]["game_id"]
        self.game_group_name = "chat_%s" % self.game_id

        await self.channel_layer.group_add(
            self.game_group_name, self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.game_group_name, self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        await self.channel_layer.group_send(
            self.game_group_name, {"type": "run_game", "message": message}
        )

    async def run_game(self, event):
        message = event["message"]

        await self.send(text_data=json.dumps({"message": message}))

