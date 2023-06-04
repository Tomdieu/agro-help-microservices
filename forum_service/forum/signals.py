from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Forum, ForumComment

from .serializers import ForumCommentSerializer, ForumSerializer


@receiver(post_save, sender=Forum)
def notify_all_farmers_on_new_forum(sender, instance, created, **kwargs):
    if created:
        try:
            from channels.layers import get_channel_layer
            from asgiref.sync import async_to_sync
            import asyncio, json

            forum_data = ForumSerializer(instance, context={"request": None}).data

            message: dict = {"msg_type": "forum_created", "data": forum_data}

            # with get_channel_layer() as channel_layer:
            channel_layer = get_channel_layer()

            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(
                channel_layer.group_send(
                    f"public_forum",
                    {"type": "send_message", "message": json.loads(message)},
                )
            )
        except:
            pass


@receiver(post_save, sender=ForumComment)
def notify_a_forum_on_new_comment(sender, instance, created, **kwargs):
    from channels.layers import get_channel_layer
    from asgiref.sync import async_to_sync
    import asyncio, json

    forum_comment = ForumCommentSerializer(instance, context={"request": None}).data
    if created:
        try:
            message: dict = {"msg_type": "forum_commented", "data": forum_comment}

            # with get_channel_layer() as channel_layer:
            channel_layer = get_channel_layer()

            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(
                channel_layer.group_send(
                    f"public_forum",
                    {"type": "send_message", "message": json.loads(message)},
                )
            )

        except:
            pass
