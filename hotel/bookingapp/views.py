from django.shortcuts import render
from django.http import request

from .models import Room

# Create your views here.


def index(request):
    rooms = Room.objects.all()
    return render(request, 'bookingapp/index.html', {'rooms':rooms})