from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Menu, ComboMenu, Testimonials, InstragramPhoto, PhotoGallery, VideoOnIndex


# Register your models here.

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'get_image_list')
    list_display_links = ('name',)
    readonly_fields = ('get_image',)
    save_on_top = True
    save_as = True

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="150" height="150">')

    get_image.short_description = 'Изображение'

    def get_image_list(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="60" height="60">')

    get_image_list.short_description = 'Изображение'


@admin.register(ComboMenu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'get_image_list')
    list_display_links = ('name',)
    readonly_fields = ('get_image',)
    save_on_top = True
    save_as = True

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="250" height="150">')

    get_image.short_description = 'Изображение'

    def get_image_list(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="100" height="60">')

    get_image_list.short_description = 'Изображение'


@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_photo_list')
    list_display_links = ('name',)
    readonly_fields = ('get_photo',)
    save_on_top = True
    save_as = True

    def get_photo(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="150" height="150">')

    get_photo.short_description = 'Фото'

    def get_photo_list(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="60" height="60">')

    get_photo_list.short_description = 'Фото'


@admin.register(InstragramPhoto)
class InstragramAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'get_photo_list')
    readonly_fields = ('get_photo',)
    save_as = True

    def get_photo(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="150" height="150">')

    get_photo.short_description = 'Фото'

    def get_photo_list(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="60" height="60">')

    get_photo_list.short_description = 'Фото'


@admin.register(PhotoGallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_photo_list')
    readonly_fields = ('get_photo',)
    save_as = True

    def get_photo(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="150" height="150">')

    get_photo.short_description = 'Фото'

    def get_photo_list(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="60" height="60">')

    get_photo_list.short_description = 'Фото'


admin.site.register(VideoOnIndex)

