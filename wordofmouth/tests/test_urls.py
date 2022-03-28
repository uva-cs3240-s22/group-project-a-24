from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from wordofmouth.views import view_recipes, create_recipe


class TestUrls(SimpleTestCase):
    def test_create_url_is_resolved(self):
        url = reverse('wordofmouth:create-recipe')
        print(resolve(url))

    def test_home_url_is_resolved(self):
        url = reverse('wordofmouth:home')
        print(resolve(url))
