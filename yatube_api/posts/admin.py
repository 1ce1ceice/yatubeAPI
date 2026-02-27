from django.contrib import admin

from .models import Comment, Group, Post


@admin.register(Comment, Group, Post)
class PostAdmin(admin.ModelAdmin):
    pass
