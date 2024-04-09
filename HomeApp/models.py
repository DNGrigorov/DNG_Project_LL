from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils import timezone
from AccountApp.models import WebUser

class Post(models.Model):
    POST_TYPES = [
        ('movie_quote', 'Movie Quote'),
        ('book_quote', 'Book Quote'),
        ('cafe_sign', 'Cafe Sign'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(WebUser, on_delete=models.CASCADE)
    content = models.TextField()
    type_of_post = models.CharField(max_length=20, choices=POST_TYPES, default='other')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username}'s {self.get_type_of_post_display()} post at {self.created_at}"