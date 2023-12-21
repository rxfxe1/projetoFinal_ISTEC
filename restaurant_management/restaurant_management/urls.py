from django.contrib import admin
from django.urls import include, path
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('orders/', include('orders.urls')),
    path('reservations/', include('reservations.urls')),
    path('tables/', include('tables.urls')),
    path('users/', include('users.urls')),
]
