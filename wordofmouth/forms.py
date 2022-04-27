from django import forms
from .models import Comment, ForkedRecipe

class RecipeForm(forms.Form):
    title = forms.CharField(label='Enter Recipe Title', max_length=200)
    description = forms.CharField(label='Enter a Brief Description', max_length=200)
    ingredients = forms.CharField(label='Enter Ingredients and Specified Amounts',widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    directions = forms.CharField(label='Enter Directions',widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    image = forms.ImageField(label='Upload Image')

class ForkedRecipeForm(forms.ModelForm):
    class Meta:
        model = ForkedRecipe
        fields = ['title', 'description', 'ingredients', 'directions', 'image']
        def __str__(self):
            return model.title
    title = forms.CharField(initial = Meta.model.title, max_length=200)
    description = forms.CharField(label='Enter a Brief Description', max_length=200)
    ingredients = forms.CharField(label='Enter Ingredients and Specified Amounts',widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    directions = forms.CharField(label='Enter Directions',widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    image = forms.ImageField(label='Upload Image')

class CommentForm(forms.ModelForm):
    class Meta:
       model = Comment
       fields = ['body']
