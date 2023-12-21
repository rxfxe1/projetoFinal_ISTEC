from django.shortcuts import render
from .models import UserProfile

def profile_detail(request, username):
    profile = UserProfile.objects.get(user__username=username)
    return render(request, 'users/profile_detail.html', {'profile': profile})