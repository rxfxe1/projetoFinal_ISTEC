from django.shortcuts import render, redirect
from reservations.models import Reservation

def index(request):
    return render(request, '../templates/base.html')

def reserve_table(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        date  = request.method.POST.get('date')
        time = request.method.POST.get('time')

        reservation = Reservation.objects.create(name=name, phone=phone, date=date, time=time)
        return redirect('index')
    
    return render(request, 'reservation/reserve_table.html')