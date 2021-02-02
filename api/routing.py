from django.urls import path
from api import consumers

ws_urlpatterns = [
    path('ws/runcode/<int:uid>/', consumers.CodeRunConsumer.as_asgi())
]
