from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'wordofmouth'
urlpatterns = [
    # ex. /wordofmouth/
    # path('', TemplateView.as_view(template_name="index.html")),
    path('', views.view_recipes, name='home'),
    path('create-recipe/', views.create_recipe, name='create-recipe'),
    # path('view-recipes/', views.view_recipes, name='view-recipes'),
]