# Generated by Django 3.2.5 on 2021-07-25 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20210725_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='photogallery',
            name='css_style',
            field=models.CharField(choices=[('Small', 'small_img'), ('Big', 'big_img')], default='Small', max_length=255, verbose_name='Стиль CSS'),
        ),
    ]
