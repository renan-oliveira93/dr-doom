from django.contrib import admin

from apps.customization.models import Customization, Styles, Logo

@admin.register(Styles)
class StylesAdmin(admin.ModelAdmin):
    list_display = ['primary_color', 'secondary_color', 'tertiary_color']

@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ['logo']

@admin.register(Customization)
class CustomizationAdmin(admin.ModelAdmin):
    list_display = ['id', 'styles', 'logo']