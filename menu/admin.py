from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Menu
# Register your models here.

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display =('id', 'name', 'price', 'get_image_list')
    list_display_links = ('name',)
    readonly_fields =('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="150" height="150">')
    get_image.short_description = 'Изображение'

    def get_image_list(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="60" height="60">')

    get_image_list.short_description = 'Изображение'