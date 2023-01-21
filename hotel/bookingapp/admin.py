from django.contrib import admin
from .models import Room, Booking

# Registration of models
admin.site.register(Room)
admin.site.register(Booking)