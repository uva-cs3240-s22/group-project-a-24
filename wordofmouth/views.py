from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from django.urls import reverse
from django.views import generic

from wordofmouth.forms import RecipeForm
from wordofmouth.models import Recipe

@login_required(login_url='/accounts/google/login')
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            r = Recipe(title=form.cleaned_data['title'],
                       description=form.cleaned_data['description'],
                       ingredients=form.cleaned_data['ingredients'],
                       directions=form.cleaned_data['directions'],
                       author=request.user)
            r.save()
            return HttpResponseRedirect('/')
    else:
        form = RecipeForm()
    return render(request, 'templates/wordofmouth/create-recipe.html', {'form': form})


def view_recipes(request):
    latest_recipe_list = Recipe.objects
    return render(request, 'templates/wordofmouth/recipe-list.html', {'latest_recipe_list': latest_recipe_list.all(), })


class RecipesByUserView(generic.ListView):
    model = Recipe
    template_name = 'templates/wordofmouth/user-recipe-list.html'
    context_object_name = 'latest_user_recipe_list'

    def get_queryset(self):
        return Recipe.objects.filter(author=self.kwargs['pk'])

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['latest_user'] = Recipe.objects.all()
    #     return context
