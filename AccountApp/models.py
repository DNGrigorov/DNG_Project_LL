from django.contrib.auth.models import AbstractUser
from django.db import models



class WebUser(AbstractUser):

    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    birth_year = models.CharField(max_length=4)
    birth_month = models.CharField(max_length=2)
    birth_day = models.CharField(max_length=2)
    gender = models.CharField(max_length=1)

    def __str__(self):
        return self.email
