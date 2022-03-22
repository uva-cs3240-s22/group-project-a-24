from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
from django.contrib.auth.models import User

from wordofmouth.models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'author')
    actions = None

    def save_model(self, request, obj, form, change):
        if not obj.author:
            obj.author = request.user
        obj.save()

#
# class AuthorInline(admin.StackedInline):
#     model = Author
#     can_delete = False
#     verbose_name_plural = 'author'
#
#
# class UserAdmin(BaseUserAdmin):
#     inlines = (AuthorInline, )


admin.site.register(Recipe, RecipeAdmin)
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)