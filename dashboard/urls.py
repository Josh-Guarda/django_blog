from django.urls import path
from . import views

from django.conf import settings # import this for dynamic path for media
from django.conf.urls.static import static # import this for dynamic path for media

urlpatterns = [
    path('',views.dashboard,name='dashboard')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
