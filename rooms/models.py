from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models


class AbstractItem(core_models.TimeStampedModel):

    """Abstract Item"""

    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class RoomType(AbstractItem):

    """Room Type Model Definition"""

    class Meta:
        verbose_name_plural = "Room Type"
        ordering = ["name"]


class Amenity(AbstractItem):

    """Amenity Object Definition"""

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    """Facility Model Definition"""

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    """House Rule Model Definition"""

    class Meta:
        verbose_name_plural = "House Rules"


class Room(core_models.TimeStampedModel):

    """Room Model Definitiion"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=100)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    max_guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(
        user_models.User, on_delete=models.CASCADE, related_name="rooms"
    )

    room_type = models.ForeignKey(
        RoomType, on_delete=models.SET_NULL, null=True, related_name="rooms"
    )
    amenities = models.ManyToManyField(Amenity, blank=True, related_name="rooms")
    facilities = models.ManyToManyField(Facility, blank=True, related_name="rooms")
    house_rules = models.ManyToManyField(HouseRule, blank=True, related_name="rooms")

    def __str__(self):
        return self.name


class Photo(core_models.TimeStampedModel):

    """Photo Model Definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="photos")

    def __str__(self):
        return self.caption
