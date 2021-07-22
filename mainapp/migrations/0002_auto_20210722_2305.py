# Generated by Django 3.2.5 on 2021-07-22 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComboMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='menu/', verbose_name='Фото')),
                ('price', models.PositiveSmallIntegerField(blank=True, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Комбо набор',
                'verbose_name_plural': 'Комбо наборы',
            },
        ),
        migrations.AlterModelOptions(
            name='menu',
            options={'verbose_name': 'Меню', 'verbose_name_plural': 'Меню'},
        ),
    ]
