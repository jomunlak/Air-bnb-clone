from django.db import models
from core import models as core_models
from users.models import User
from rooms.models import Room


class Review(core_models.TimeStampedModel):

    """Review Model Definition"""

    content = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    room = models.ForeignKey(Room, on_delete=models.CASCADE,  related_name="reviews")

    def __str__(self):
        return f"{self.content} - {self.room}"
