# Generated by Django 3.2 on 2021-06-10 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_and_company', '0011_auto_20210610_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='images',
        ),
        migrations.RemoveField(
            model_name='person',
            name='img',
        ),
    ]
