from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import index, reserve_table
from reservations.views import ReservationViewSet  # Update this import

router = DefaultRouter()
router.register(r'reservations', ReservationViewSet, basename='reservation')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('orders/', include('orders.urls')),
    path('reservations/', include('reservations.urls')),
    path('tables/', include('tables.urls')),
    path('users/', include('users.urls')),
    path('reserve/', reserve_table, name='reserve_table'),
    path('api/', include(router.urls)),
]
