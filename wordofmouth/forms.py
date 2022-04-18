from django import forms
from wordofmouth.models import Comment

class RecipeForm(forms.Form):
    title = forms.CharField(label='Enter Recipe Title', max_length=200)
    description = forms.CharField(label='Enter a Brief Description', max_length=200)
    ingredients = forms.CharField(label='Enter Ingredients and Specified Amounts',widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    directions = forms.CharField(label='Enter Directions',widget=forms.Textarea(attrs={"rows":5, "cols":20}))

class CommentForm(forms.ModelForm):
    class Meta:
       model = Comment
       fields = ('author', 'body')