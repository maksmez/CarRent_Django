# Generated by Django 3.2 on 2021-06-12 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='Status',
            field=models.IntegerField(blank=True, null=True, verbose_name='Статус заказа'),
        ),
    ]
