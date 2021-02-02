from django.urls import path
from api import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.upload_tc),
    path('getData/', views.getData),
    path('run/<int:uid>/', views.runCode)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)