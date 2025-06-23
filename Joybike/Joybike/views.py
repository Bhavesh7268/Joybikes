from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,"index.html")
def login(request):
    return render(request,"login.html")
def Register(request):
    return render(request,"Register.html")
@login_required
def profile_view(request):
    return render(request, 'profile.html', {
        'user': request.user  # Pass the user object to template
    })