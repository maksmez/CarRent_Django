# Generated by Django 3.2 on 2021-05-03 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CompanyID', models.IntegerField(verbose_name='ID Компании')),
                ('Location', models.CharField(max_length=250, verbose_name='Расположение')),
                ('Photo', models.JSONField(verbose_name='Фото')),
                ('RentCondition', models.TextField(verbose_name='Условия аренды')),
                ('Header', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('Driver', models.BooleanField(verbose_name='Водитель')),
                ('Status', models.BooleanField(verbose_name='Статус')),
                ('CategoryID', models.IntegerField(verbose_name='ID Категории')),
                ('CategoryVUID', models.IntegerField(verbose_name='Категория ВУ')),
                ('DateDel', models.DateField(verbose_name='Дата удаления')),
                ('FixedRate', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Фиксированная ставка')),
                ('Percent', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Комиссия')),
                ('Brand_and_name', models.CharField(max_length=150, verbose_name='Марка и модель')),
                ('transmission', models.CharField(max_length=60, verbose_name='Коробка')),
                ('engine', models.CharField(max_length=60, verbose_name='Двигатель')),
                ('car_type', models.CharField(max_length=60, verbose_name='Кузов')),
                ('drive', models.CharField(max_length=60, verbose_name='Привод')),
                ('year', models.IntegerField(verbose_name='Год')),
                ('power', models.IntegerField(verbose_name='Мощность')),
                ('price', models.IntegerField(verbose_name='Стоимость')),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
            },
        ),
    ]
