from django.contrib import admin
from django.urls import include, path
from .views import index, reserve_table

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('orders/', include('orders.urls')),
    path('reservations/', include('restaurant_management.reservations.urls')),
    path('tables/', include('tables.urls')),
    path('users/', include('users.urls')),
    path('reserve/', reserve_table, name='reserve_table'),
]
