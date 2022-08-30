from django.contrib import admin
from django.utils.html import mark_safe
from . import models
from rooms import models as room_models


@admin.register(
    models.RoomType,
    models.Amenity,
    models.Facility,
    models.HouseRule,
)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()


class PhotoInline(admin.StackedInline):
    model = room_models.Photo


@admin.register(models.Room)
class CustomRoomAdmin(admin.ModelAdmin):

    """Custom Room Admin"""

    inlines = [
        PhotoInline,
    ]

    fieldsets = (
        (
            "Basic Info",
            {
                "classes": ("collapse",),
                "fields": (
                    "name",
                    "description",
                    "country",
                    "address",
                    "price",
                    "city",
                ),
            },
        ),
        (
            "Times",
            {
                "fields": (
                    "check_in",
                    "check_out",
                    "instant_book",
                )
            },
        ),
        (
            "Spaces",
            {
                "fields": (
                    "max_guests",
                    "beds",
                    "bedrooms",
                    "baths",
                )
            },
        ),
        (
            "More about the spaces",
            {
                "fields": (
                    "amenities",
                    "facilities",
                    "house_rules",
                )
            },
        ),
        ("Details", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "host",
        "country",
        "city",
        "price",
        "address",
        "max_guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
        "created",
        "updated",
    )
    list_filter = (
        "instant_book",
        "host__superhost",
        "city",
        "country",
    )
    search_fields = (
        "city",
        "country",
    )

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )
    ordering = ("created",)

    raw_id_fields = ("host",)

    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()

    count_amenities.short_description = "Amenities"
    count_photos.short_description = "Photos"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    list_display = [
        "__str__",
        "get_thumbnail",
    ]

    def get_thumbnail(self, obj):
        return mark_safe(f"<img width='50px' src={obj.file.url}/>")

    get_thumbnail.short_description = "Thumbnail"
