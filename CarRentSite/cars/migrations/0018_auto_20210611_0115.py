# Generated by Django 3.2 on 2021-06-10 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0017_auto_20210610_2248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='CategoryVUID',
        ),
        migrations.AddField(
            model_name='car',
            name='CategoryVU',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Категория ВУ'),
        ),
    ]
