from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# db 모델 설정


class User(AbstractUser):

    """Custom User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    bio = models.TextField(default="", blank=True)
    avatar = models.ImageField(blank=True)
    gender = models.CharField(
        max_length=10, null=True, choices=GENDER_CHOICES, default="Female"
    )
