from django.conf import settings
from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Temp(models.Model):
    temp_date = models.DateTimeField('date published')

    def __str__(self):
        return self.temp_date

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.temp_date <= now


# class Author(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Recipe(models.Model):
    title = models.CharField(max_length=100, blank=False) # double check on blank
    description = models.CharField(max_length=175, blank=True)
    ingredients = models.TextField(blank = True)
    directions = models.TextField(blank = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title
