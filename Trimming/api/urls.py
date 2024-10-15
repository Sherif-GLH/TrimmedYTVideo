from django.urls import path
from .views import TrimView , download
urlpatterns = [
    path('video/', TrimView.as_view(), name='video'),
    path('videodown/<str:id>/', download, name='down'),
]
