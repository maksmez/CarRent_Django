# Generated by Django 3.2 on 2021-06-13 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'Сообщение', 'verbose_name_plural': 'Сообщения'},
        ),
        migrations.AlterField(
            model_name='message',
            name='Date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата'),
        ),
    ]
