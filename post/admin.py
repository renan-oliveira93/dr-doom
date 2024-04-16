from django.contrib import admin
from post.models import Post

class Posts(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

admin.site.register(Post, Posts)