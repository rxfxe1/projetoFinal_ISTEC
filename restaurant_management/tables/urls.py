from django.urls import path
from .views import table_list

urlpatterns = [
    path('list/', table_list, name='table_list'),    
]