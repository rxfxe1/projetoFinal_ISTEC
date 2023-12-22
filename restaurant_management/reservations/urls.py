from django.urls import path
from .views import ReservationListCreateView, ReservationViewSet

urlpatterns = [
    path('list/', ReservationListCreateView.as_view(), name='reservation-list-create'),
    path('detail/<int:pk>/', ReservationViewSet.as_view({'get': 'retrieve'}), name='reservation-detail'),
]
