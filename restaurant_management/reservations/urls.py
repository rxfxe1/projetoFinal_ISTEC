from django.urls import path
from .views import reservation_list, reserve_table

urlpatterns = [
    path('list/', reservation_list, name='reservation_list'),
    path('reserve/', reserve_table, name='reserve_table')  
]