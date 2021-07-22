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
