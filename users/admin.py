from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


# Register your models here.
# admin 패널에 반영되는 내용


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""

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
