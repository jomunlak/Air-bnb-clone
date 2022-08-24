from django.db import models

# Create your models here.


class List(models.Model):

    """List Model Definition"""

    name = models.CharField(max_length=80)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ManyToManyField("rooms.Room", blank=True)

    def __str__(self):
        return len(self.room)
