# Generated by Django 3.2 on 2021-05-04 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='Photo',
            field=models.CharField(max_length=250, verbose_name='Фото'),
        ),
    ]
