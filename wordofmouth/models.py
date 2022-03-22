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


class Recipe(models.Model):
    title = models.CharField(max_length=100, blank=False) # double check on blank
    description = models.CharField(max_length=175, blank=True)
    # ingredients = ArrayField(models) fix later
    # directions =  fix later
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title


