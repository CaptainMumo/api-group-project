from django .db import models
from django.conf import settings
# Create models


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


def _str_(self):
    return f'{self.number}.{self.category} with {self.beds} beds for {self.capacity} people'


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def _str_(self):
        return f'{self.user} has booked {self.room} from {self.check_in} to {self.check_out}'
