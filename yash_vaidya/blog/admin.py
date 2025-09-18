from django.contrib import admin
from .models import blog_post

# Register your models here.
# This PostAdmin helps to give you more easy UI for you admin or post.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created_at')
    list_filter = ('status', 'created_at', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}  # auto-fill slug from title

admin.site.register(blog_post, PostAdmin)
