from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from . import models as room_models

# Create your views here.


def all_rooms(request):
    all_rooms = room_models.Room.objects.all()
    return render(request, "rooms/all_rooms.html", context={"rooms": all_rooms})
