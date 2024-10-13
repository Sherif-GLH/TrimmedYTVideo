from django.urls import path
from .views import TrimView
urlpatterns = [
    path('video/', TrimView.as_view(), name='video'),
]
