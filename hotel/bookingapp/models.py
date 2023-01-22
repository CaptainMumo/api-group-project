from django .db import models
from django.conf import settings
# Create models

class Guest(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('P', 'Prefer Not Say'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=GENDER)
    dob = models.DateField(name='Date of Birth')
    phone_no = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.user}'

class Room (models.Model):
    ROOM_CATEGORIES = (
        ('AC', 'AC'),
        ('NON-AC', 'NON-AC'),
        ('DELUXE', 'DELUXE'),
        ('KING', 'KING'),
        ('QUEEN', 'QUEEN'),
    )
    number = models.IntegerField()
    category = models.CharField(max_length=7, choices=ROOM_CATEGORIES)
    beds = models.IntegerField()
    capacity = models.IntegerField()

    # function

    def __str__(self):
        return f'{self.number} -> {self.category} with {self.beds} beds for {self.capacity} people'


class Booking(models.Model):
    user = models.ForeignKey(Guest,
                             on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'{self.user} has booked {self.room} from {self.check_in} to {self.check_out}'
