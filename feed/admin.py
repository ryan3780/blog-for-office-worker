from django.contrib import admin
from .models import Article, Comment, HashTag

@admin.register(Article, Comment, HashTag)
class FeedAdmin(admin.ModelAdmin):
    pass
