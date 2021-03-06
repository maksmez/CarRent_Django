# Generated by Django 3.2 on 2021-06-10 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_and_company', '0010_alter_person_categoryvu'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='images',
            field=models.JSONField(blank=True, default='{}', null=True, verbose_name='Картинки'),
        ),
        migrations.AddField(
            model_name='person',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='test'),
        ),
    ]
