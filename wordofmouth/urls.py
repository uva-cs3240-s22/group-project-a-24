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
    path('recipe/<int:id>/fork-recipe/', views.fork_recipe, name='fork-recipe'),
    # path('view-recipes/', views.view_recipes, name='view-recipes'),
    path('<int:pk>/recipes', views.RecipesByUserView.as_view(), name='recipes-by-user'),
    path('recipe/<int:id>', views.recipe_detail, name='recipe-detail'),
    path('favorites', views.UserFavorites.as_view(), name = 'favorite_list'),
    path('favorite/<int:id>', views.add_favorite, name='add-recipe-favorite'),
]