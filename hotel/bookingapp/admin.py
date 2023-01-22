from django.contrib import admin
from .models import Room, Booking, Guest

# Registration of models
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Guest)