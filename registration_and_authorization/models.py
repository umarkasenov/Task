from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class CustomUser(User):
    GENDER_CHOICES = (
        ("M", "Мужской"),
        ("F", "Женский"),
        ("IT", "Другое")
    )
    STATUS_CHOICES = (
        ("В сети", "В сети"),
        ("Занят", "Занят"),
        ("На работе", "На работе"),
        ("В школе", "В школе")
    )
    age = models.PositiveIntegerField(validators=[MinValueValidator(18), MaxValueValidator(60)])
    phone_number = models.CharField(max_length=16, default="+996")
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    bio = models.TextField(blank=True)
    social_media = models.URLField(blank=True)
    interests = models.CharField(max_length=100, blank=True)
    hobbies = models.CharField(max_length=100, blank=True)
