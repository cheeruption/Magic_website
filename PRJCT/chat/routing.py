# from channels.routing import ProtocolTypeRouter

# application = ProtocolTypeRouter({
#     # Empty for now (http->django views is added by default)
# })

# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer),
]