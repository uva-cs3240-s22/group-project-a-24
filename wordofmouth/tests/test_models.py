from django.test import TestCase
from wordofmouth.models import Recipe
from django.contrib.auth.models import User


class RecipeTestCase(TestCase):
    def setUp(self):
        Recipe.objects.create(title="Hashbrowns", description="This is a recipe on how to make my favorite hashbrowns",
                              ingredients="potatoes", directions="I actually don't know how to make hashbrowns", author=User.objects.create(username="hana"))

    def test_recipes_are_properly_stored(self):
        hashbrowns = Recipe.objects.get(title="Hashbrowns")
        self.assertEqual(hashbrowns.__str__, 'Hashbrowns')
