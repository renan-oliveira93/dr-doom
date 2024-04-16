from django.contrib import admin
from image.models import Image

class Images(admin.ModelAdmin):
    list_display = ('id', 'image_title', 'credits', 'picture_date', 'picture')
    list_display_links = ('id', 'image_title')
    search_fields = ('image_title',)
    list_per_page = 10

admin.site.register(Image, Images)