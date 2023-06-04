from django.urls import re_path
from . import consumers


websocket_urpatterns = [
    re_path(
        r"ws/forum_chat/(?P<forum_id>[0-9]+)/$",
        consumers.PublicForumConsumer.as_asgi(),
    ),
    re_path(r"ws/public_forum/$", consumers.ForumConsumer.as_asgi()),
]
