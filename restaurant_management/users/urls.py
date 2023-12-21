from django.urls import path
from .views import profile_detail

urlpatterns = [
    path('profile/<str:username>/', profile_detail, name='profile_detail'),
]