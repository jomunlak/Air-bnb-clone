from django.contrib import admin
from . import models

# Register your models here.

# admin 패널에 반영되는 내용


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    pass
