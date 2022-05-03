# REFERENCES
# https://stackoverflow.com/questions/4733609/how-do-i-clone-a-django-model-instance-object-and-save-it-to-the-database

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from django.urls import reverse
from django.views import generic

from wordofmouth.forms import RecipeForm, CommentForm, ForkedRecipeForm
from wordofmouth.models import Recipe, Comment, FavoriteRecipe

from django.shortcuts import get_object_or_404, redirect


@login_required(login_url='/accounts/google/login')
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            r = Recipe(title=form.cleaned_data['title'],
                       description=form.cleaned_data['description'],
                       ingredients=form.cleaned_data['ingredients'],
                       directions=form.cleaned_data['directions'],
                       author=request.user,
                       image=request.FILES['image'],
                       )
            r.save()
            return HttpResponseRedirect('/')
    else:
        form = RecipeForm()
    return render(request, 'templates/wordofmouth/create-recipe.html', {'form': form})


@login_required(login_url='/accounts/google/login')
def fork_recipe(request, id):
    recipe = Recipe.objects.get(pk=id)
    if request.method == 'POST':
        form = ForkedRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            r = Recipe(title=form.cleaned_data['title'],
                       description=form.cleaned_data['description'],
                       ingredients=form.cleaned_data['ingredients'],
                       directions=form.cleaned_data['directions'],
                       author=request.user,
                       image=recipe.image,
                       parent=recipe.id,
                       pk=None
                       )
            r.save()
            return HttpResponseRedirect('/')
    else:
        form = ForkedRecipeForm(instance=recipe)
    return render(request, 'templates/wordofmouth/fork-recipe.html', {'form': form, 'recipe': recipe})


def view_recipes(request):
    latest_recipe_list = Recipe.objects
    return render(request, 'templates/wordofmouth/recipe-list.html', {'latest_recipe_list': latest_recipe_list.all(), })


class RecipesByUserView(generic.ListView):
    model = Recipe
    template_name = 'templates/wordofmouth/user-recipe-list.html'
    context_object_name = 'latest_user_recipe_list'

    def get_queryset(self):
        return Recipe.objects.filter(author=self.kwargs['pk'])


def recipe_detail(request, id):
    recipe = Recipe.objects.get(id=id)
    children = Recipe.objects.filter(parent=id)
    temp = FavoriteRecipe.objects.filter(user=request.user)
    user_favs = []
    for fav in temp:
        user_favs.append(fav.recipe)
    print(user_favs)

    comments = Comment.objects.filter(recipe=recipe)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # new_comment = Comment.objects.create(recipe=recipe, user=request.user, body=request.POST.get('body'))
            new_comment = comment_form.save(commit=False)
            new_comment.recipe = recipe
            new_comment.user = request.user
            new_comment.body = request.POST.get('body')
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    return render(request, 'wordofmouth/recipe-detail.html',
                  {'recipe': recipe, 'user_favs': user_favs, 'comments': comments, 'new_comment': new_comment,
                   'comment_form': comment_form, 'children': children})

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['latest_user'] = Recipe.objects.all()
    #     return context


@login_required
def add_favorite(request, id):
    r = get_object_or_404(Recipe, id=id)
    if r.favorites.filter(user=request.user).exists():
        # check to see if the user has already added this post to favorites
        r.favorites.filter(user=request.user).delete()
    else:
        f = FavoriteRecipe.objects.create(user=request.user, recipe=r)
        f.save()
        # r.favorites.add(request.user)
    # return render(request, 'wordofmouth/user-favorites.html')
    return redirect(request.META.get('HTTP_REFERER'))

# def favorite_list(request):
#     favorites = Recipe.newmanager.filter(favorites=request.user)
#     return render(request, 'wordofmouth/user-favorites.html', { 'favorites': favorites })
# @login_required


class UserFavorites(generic.ListView):
    model = Recipe
    template_name = 'templates/wordofmouth/user-favorites.html'
    context_object_name = 'favorites'

    def get_queryset(self):
        return FavoriteRecipe.objects.filter(user=self.request.user)
