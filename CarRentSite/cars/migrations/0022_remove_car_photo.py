# Generated by Django 3.2 on 2021-06-11 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0021_car_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='Photo',
        ),
    ]
