from django.urls import path
from .views import reservation_list, reserve_table, ReservationListCreateView

urlpatterns = [
    path('list/', reservation_list, name='reservation_list'),
    path('reserve/', reserve_table, name='reserve_table'),
    path('api/reservations/', ReservationListCreateView.as_view(), name='reservation-list-create'),  # Update the name here
]
