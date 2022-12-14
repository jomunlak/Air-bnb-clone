from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

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

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, "English"), (LANGUAGE_KOREAN, "Korean"))

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))

    bio = models.TextField(default="", blank=True)
    avatar = models.ImageField(blank=True, upload_to="avatars")
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES, default="Female", blank=True
    )
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=10, blank=True, default=LANGUAGE_KOREAN
    )
    currency = models.CharField(
        max_length=3, choices=CURRENCY_CHOICES, blank=True, default=CURRENCY_KRW
    )
    superhost = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})

    def __str__(self):
        return self.username
