from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework import generics, viewsets
from .models import Reservation
from .forms import ReservationForm
from .serializers import ReservationSerializer

def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservation/reservation_list.html', {'reservations': reservations})


def reserve_table(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            messages.success(request, 'Reservation submitted successfully.')
            return redirect('reservation_list')  # Fix the typo here
    else:
        form = ReservationForm()

    return render(request, 'reservation/reserve_table.html', {'form': form})


class ReservationListCreateView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer