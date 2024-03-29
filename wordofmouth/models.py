# REFERENCES
# # https://stackoverflow.com/questions/47597174/django-get-all-objects-from-a-specific-user
# https://stackoverflow.com/questions/2991365/how-to-auto-insert-the-current-user-when-creating-an-object-in-django-admin
from django.conf import settings
from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django import urls
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
    # double check on blank
    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=175, blank=True)
    ingredients = models.TextField(blank=True)
    directions = models.TextField(blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='staticfiles',
                              default='staticfiles/recipe.png')
    parent = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title


class FavoriteRecipe(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='favorites')
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='favorites')


class Comment(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(blank=True)

    def __str__(self):
        return'Comment {} by {}'.format(self.body, self.user)
