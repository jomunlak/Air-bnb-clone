from django.db import models

# Create your models here.


class List(models.Model):

    """List Model Definition"""

    name = models.CharField(max_length=80)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="lists"
    )
    rooms = models.ManyToManyField("rooms.Room", blank=True, related_name="lists")

    def __str__(self):
        return self.name

    def count_rooms(self):
        return self.rooms.count()

    count_rooms.short_description = "Number of rooms"
