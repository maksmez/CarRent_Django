# Generated by Django 3.2 on 2021-06-10 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0019_alter_car_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='Photo',
        ),
    ]