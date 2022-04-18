from django.template.defaulttags import url
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
    path('<int:pk>/recipes', views.RecipesByUserView.as_view(), name='recipes-by-user'),
    path('<int:ID>/recipes', views.SingleRecipeView.as_view(), name='single-recipe')
]