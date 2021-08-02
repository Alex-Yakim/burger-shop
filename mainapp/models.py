from django.db import models


# Create your models here.
class Menu(models.Model):
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', blank=True)
    photo = models.ImageField('Фото', upload_to='menu/')
    price = models.PositiveSmallIntegerField('Цена', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class ComboMenu(models.Model):
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', blank=True)
    photo = models.ImageField('Фото', upload_to='menu/combo_menu')
    price = models.PositiveSmallIntegerField('Цена', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комбо набор'
        verbose_name_plural = 'Комбо наборы'


class Testimonials(models.Model):
    name = models.CharField('Имя', max_length=255)
    photo = models.ImageField('Фото', upload_to='menu/testimonials')
    text = models.TextField('Отзыв')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class InstragramPhoto(models.Model):
    photo = models.ImageField('Фото', upload_to='menu/instragram')
    url = models.URLField('url', max_length=255, blank=True)

    def __str__(self):
        return self.photo.name

    class Meta:
        verbose_name = 'Фото из Instagram'
        verbose_name_plural = 'Фото из Instagram'


class PhotoGallery(models.Model):
    IMG_SIZES = (
        ('small_img', 'Small'),
        ('big_img', 'Big'),
    )
    photo = models.ImageField('Фото', upload_to='gallery')
    css_style = models.CharField('Стиль CSS', max_length=255, choices=IMG_SIZES, default='Small')


    def __str__(self):
        return self.photo.name

    class Meta:
        verbose_name = 'Фото галлереи'
        verbose_name_plural = 'Фото галлереи'


class VideoOnIndex(models.Model):
    video = models.URLField('Ссылка на видео', max_length=200)
    title = models.CharField('Заголовок', max_length=150, blank=True)
    description = models.CharField('Описание', max_length=200, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видео на главной'
        verbose_name_plural = 'Видео на главной'
