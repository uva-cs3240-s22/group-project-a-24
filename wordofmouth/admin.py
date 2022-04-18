from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
from django.contrib.auth.models import User

from wordofmouth.models import Recipe, Comment


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'author')
    actions = None

    def save_model(self, request, obj, form, change):
        if not obj.author:
            obj.author = request.user
        obj.save()

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'post')
    filter = 'active'
    search_fields = ('author', 'body')

    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
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