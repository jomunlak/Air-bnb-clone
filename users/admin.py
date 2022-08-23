from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


# Register your models here.
# admin 패널에 반영되는 내용


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""

    list_display = UserAdmin.list_display + (
        "avatar",
        "gender",
        "birthdate",
        "bio",
        "language",
        "currency",
        "superhost",
    )
    list_filter = UserAdmin.list_filter + (
        "avatar",
        "gender",
        "birthdate",
        "bio",
        "language",
        "currency",
        "superhost",
    )
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
