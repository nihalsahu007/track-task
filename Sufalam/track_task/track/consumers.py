from channels.generic.websocket import AsyncWebsocketConsumer
import json

class TaskConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("task_updates", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("task_updates", self.channel_name)

    async def task_update(self, event):
        print(event)
        await self.send(text_data=json.dumps({
            "message": event["message"]
        }))
