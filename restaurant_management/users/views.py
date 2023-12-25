from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserProfile

@login_required
def profile_detail(request):
    user = request.user
    return render(request, 'users/profile_detail.html', {'user': user})