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
    title = models.CharField(max_length=100, blank=False) # double check on blank
    description = models.CharField(max_length=175, blank=True)
    ingredients = models.TextField(blank = True)
    directions = models.TextField(blank = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='staticfiles', default='staticfiles/recipe.png')

    def __str__(self):
        return self.title

class ForkedRecipe(models.Model):
    originalRecipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    title = Recipe.title
    description = Recipe.description
    ingredients = Recipe.ingredients
    directions = Recipe.directions
    author = Recipe.author
    image = models.ImageField(upload_to='staticfiles', default='staticfiles/recipe.png')
    ogLink = Recipe.id
    # title = models.CharField(max_length=100, blank=False, default=models.ForeignKey(Recipe, on_delete=models.CASCADE).get_foreign_related_value(Recipe)) # double check on blank
    # description = models.CharField(max_length=175, blank=True, default=models.ForeignKey(Recipe.description, on_delete=models.CASCADE))
    # ingredients = models.TextField(blank = True, default=models.ForeignKey(Recipe.ingredients, on_delete=models.CASCADE))
    # directions = models.TextField(blank = True, default=models.ForeignKey(Recipe.directions, on_delete=models.CASCADE))
    # author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=models.ForeignKey(Recipe.author, on_delete=models.CASCADE))
    # image = models.ImageField(upload_to='staticfiles', default='staticfiles/recipe.png')
    # oglink = models.ForeignKey(Recipe.pk, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class FavoriteRecipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='favorites')

class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(blank=True)

    def __str__(self):
       return'Comment {} by {}'.format(self.body, self.user)