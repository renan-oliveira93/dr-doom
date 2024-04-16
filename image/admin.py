from django.contrib import admin
from image.models import Image

class Images(admin.ModelAdmin):
    list_display = ('id', 'title', 'credits', 'picture_date', 'picture')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

admin.site.register(Image, Images)