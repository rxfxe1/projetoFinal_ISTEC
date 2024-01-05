from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView
from rest_framework.routers import DefaultRouter
from .views import index, reserve_table
from reservations.views import ReservationViewSet

router = DefaultRouter()
router.register(r'reservations', ReservationViewSet, basename='reservation')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('orders/', include('orders.urls')),
    path('reservations/', include('reservations.urls')),
    path('tables/', include('tables.urls')),
    path('reserve/', reserve_table, name='reserve_table'),
    path('api/', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('auth/', include('authentication.urls')),
]
