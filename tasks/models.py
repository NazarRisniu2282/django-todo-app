from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    bio = models.TextField(max_length=200, null=True, blank=True)
    avatar = models.ImageField(
        upload_to="avatar/", blank=True, default="avatar/avatar.svg"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    password = models.CharField(max_length=120, null=True, blank=True)
    participants = models.ManyToManyField(User, related_name="joined_rooms", blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name="tasks", null=True
    )
    host = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    time_created = models.TimeField(auto_now_add=True)
    due_to_time = models.TimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    PRIORITY_CHOICES = [
        ("L", "Low"),
        ("M", "Medium"),
        ("H", "High"),
    ]
    priority = models.CharField(
        max_length=1, choices=PRIORITY_CHOICES, default="M"
        )

    def __str__(self):
        return self.name


class Messages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, null=True, related_name="messages"
    )
    body = models.TextField(max_length=200)
    created_at = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:50]
