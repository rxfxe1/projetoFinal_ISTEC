from django.urls import path
from .views import reservation_list

urlpatterns = [
    path('list/', reservation_list, name='reservation_list'),    
]