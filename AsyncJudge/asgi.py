import django
django.setup()
import os
from decouple import config
from django.core.asgi import get_asgi_application
from api.routing import ws_urlpatterns

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AsyncJudge.settings')
#application = get_default_application()


application = ProtocolTypeRouter({
    'http' : get_asgi_application(),
    'websocket' : AuthMiddlewareStack(URLRouter(ws_urlpatterns))
})
