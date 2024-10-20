from django.urls import path
from .views import TrimView , download , test_twitter 
urlpatterns = [
    path('video/', TrimView.as_view(), name='video'),
    path('videodown/<str:id>/', download, name='down'),
    path('twitter/', test_twitter, name='twitter'),
]
