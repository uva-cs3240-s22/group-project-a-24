from django.test import TestCase, Client
from wordofmouth.views import RecipesByUserView, RecipeForm, view_recipes, create_recipe
from django.urls import reverse
from wordofmouth.models import Recipe, User


class Testviews(TestCase):  # tests based off of this tutorial: https://www.youtube.com/watch?v=hA_VxnxCHbo&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM&index=3
    def setup(self):
        self.client = Client()
        self.coolRecipe = Recipe.objects.create(
            title="mochi donuts",
            description="it's the best of both worlds.",
            ingredients="glutinous rice flour, sugar, oil, etc",
            directions="consult some other website for a recipe HAHA",
            author=User.objects.create(username="hana")
        )

    # def test_something_POST(self):
    #     RecipeForm.objects.create(
    #         title= coolRecipe.title,
    #         description=form.cleaned_data['description'],
    #         ingredients=form.cleaned_data['ingredients'],
    #         directions=form.cleaned_data['directions'],
    #         author=request.user
    #     )
