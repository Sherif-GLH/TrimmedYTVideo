from django.urls import path
<<<<<<< HEAD
from .views import TrimView , download , test_twitter 
urlpatterns = [
    path('video/', TrimView.as_view(), name='video'),
    path('videodown/<str:id>/', download, name='down'),
    path('twitter/', test_twitter, name='twitter'),
=======
from .views import TrimView
urlpatterns = [
    path('video/', TrimView.as_view(), name='video'),
    
>>>>>>> 91fafc1da8f3248d36e1cc024953e7ed46570d36
]
