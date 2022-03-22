from django import forms


class RecipeForm(forms.Form):
    title = forms.CharField(label='Enter Recipe Title', max_length=200)
    description = forms.CharField(label='Enter a Brief Description', max_length=200)