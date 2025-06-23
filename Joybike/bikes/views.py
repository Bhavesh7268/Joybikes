from django.shortcuts import render, get_object_or_404
from .models import Bike



def home(request):
    # Your home page logic here
    return render(request, 'index.html')

def bike_detail(request, pk):
    bike = get_object_or_404(Bike, pk=pk)
    context = {
        'bike': bike,
    }
    return render(request, 'bikes/bike_detail.html', context)