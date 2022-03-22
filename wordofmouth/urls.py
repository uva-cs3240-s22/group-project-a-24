from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'wordofmouth'
urlpatterns = [
    # ex. /wordofmouth/
    path('', TemplateView.as_view(template_name="index.html")),
    path('create-recipe/', views.create_recipe, name='create-recipe'),
]