from django.db import models
from core.models import TimeStampedModel
from users.models import User
from rooms.models import Room

# Create your models here.


class Reservation(TimeStampedModel):
    """Reservation Model Definition"""

    STATUS_PEDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PEDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELED, "Canceled"),
    )

    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=STATUS_PEDING
    )
    guest = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="resevations"
    )
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="resevations")
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"{self.room} - {self.check_in}"
