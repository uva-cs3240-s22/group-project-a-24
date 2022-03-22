from django.contrib import admin

# Register your models here.
from wordofmouth.models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'author')
    actions = None

    def save_model(self, request, obj, form, change):
        if not obj.author:
            obj.author = request.user
        obj.save()


admin.site.register(Recipe, RecipeAdmin)