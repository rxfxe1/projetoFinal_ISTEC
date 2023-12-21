from django.urls import path
from .views import order_list

urlpatterns = [
    path('list/', order_list, name='order_list'),
]
