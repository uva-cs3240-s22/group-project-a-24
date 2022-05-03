# REFERENCES
# https://www.youtube.com/watch?v=qwypH3YvMKc&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM&index=1
# https://www.youtube.com/watch?v=0MrgsYswT1c&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM&index=2
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
