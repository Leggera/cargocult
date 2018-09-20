# Generated by Django 2.1.1 on 2018-09-20 17:03

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10, verbose_name='Номер')),
                ('start_date', models.DateField(verbose_name='Дата выдачи')),
                ('end_date', models.DateField(verbose_name='Дата окончания')),
                ('remaining_trips', models.IntegerField(default=10, verbose_name='Число оставшихся поездок')),
            ],
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('latitude', models.FloatField(verbose_name='Широта')),
                ('longitude', models.FloatField(verbose_name='Долгота')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Название маршрута')),
                ('points_array', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_plate', models.CharField(blank=True, max_length=10, null=True, verbose_name='Номерной знак')),
                ('capacity', models.FloatField(verbose_name='Вместимость')),
            ],
        ),
        migrations.AddField(
            model_name='license',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cargocult.Route'),
        ),
        migrations.AddField(
            model_name='license',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cargocult.Track'),
        ),
    ]
