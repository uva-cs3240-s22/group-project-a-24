from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from wordofmouth.forms import RecipeForm
from wordofmouth.models import Recipe

@login_required(login_url='/accounts/google/login')
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            r = Recipe(title=form.cleaned_data['title'], description=form.cleaned_data['description']) #, user_name=form.cleaned_data['user_name'])
            r.save()
            return HttpResponseRedirect('/')
    else:
        form = RecipeForm()
    return render(request, 'templates/wordofmouth/create-recipe.html', {'form': form})


def view_recipes(request):
    latest_recipe_list = Recipe.objects
    return render(request, 'templates/wordofmouth/recipe-list.html', {'latest_recipe_list': latest_recipe_list.all(), })