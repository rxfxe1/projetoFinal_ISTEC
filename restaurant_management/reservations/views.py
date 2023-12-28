from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from rest_framework import generics, viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
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
            return redirect('reservation_list')
    else:
        form = ReservationForm()

    return render(request, 'reservation/reserve_table.html', {'form': form})


class ReservationListCreateView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def registration_view(request):
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    email = request.data.get('email')
    phone = request.data.get('phone')
    username = request.data['username']
    password = request.data['password']

    if not (first_name and last_name and email and phone and username and password):
        return Response({'error':'All fields are required.'},status=status.HTTP_400_BAD_REQUEST)
    
    user, created = User.objects.get_or_create(
        username=username,
        defaults={'first_name': first_name, 'last_name': last_name, 'email': email}
    )
    if created:
        user.set_password(password)
        user.save()
        return Response({'success': 'User registered successfully.'}, status=status.HTTP_201_CREATED)
    else:
        return Response({'error':'Username already exists.'},status=status.HTTP_400_BAD_REQUEST)
    