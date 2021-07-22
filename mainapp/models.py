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
