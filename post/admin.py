from django.contrib import admin
from post.models import Post

class Posts(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'category', 'published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'category','published')
    list_per_page = 10

admin.site.register(Post, Posts)