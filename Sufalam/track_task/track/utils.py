from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def send_notification(message):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "task_updates",  # this should match the group name in consumer
        {
            "type": "task_update",
            "message": message
        }
    )
    print(message)