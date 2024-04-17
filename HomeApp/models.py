from ckeditor.fields import RichTextField
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
    content = RichTextField()
    type_of_post = models.CharField(max_length=20, choices=POST_TYPES, default='other')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        time_str = self.created_at.strftime("%I:%M %p on %d-%m-%Y")
        return f"{self.user.username} posted a {self.get_type_of_post_display()} at {time_str}"

class OriginalPostContent(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = RichTextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Original content of {self.post} created at {self.created_at}"

class Comment(models.Model):
    user = models.ForeignKey(WebUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = RichTextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post}"

class PostVersion(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='versions')
    user = models.ForeignKey(WebUser, on_delete=models.SET_NULL, null=True)
    content = RichTextField()
    timestamp = models.DateTimeField(default=timezone.now)

