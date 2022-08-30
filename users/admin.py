from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from rooms import models as room_models

# Register your models here.
# admin 패널에 반영되는 내용


class RoomInline(admin.TabularInline):
    model = room_models.Room


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""

    inlines = [
        RoomInline,
    ]

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )
    list_filter = UserAdmin.list_filter + ("superhost",)
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom fieldsets",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "birthdate",
                    "bio",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
