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

class LanguageSkill(models.Model):
    user = models.OneToOneField(WebUser, on_delete=models.CASCADE)
    english_skill = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    german_skill = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    japanese_skill = models.DecimalField(max_digits=3, decimal_places=1, default=0)

class Rating(models.Model):
    rater = models.ForeignKey(WebUser, related_name='ratings_given', on_delete=models.CASCADE)
    rated_user = models.ForeignKey(WebUser, related_name='ratings_received', on_delete=models.CASCADE)
    language = models.CharField(max_length=20)
    stars = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.rater.username