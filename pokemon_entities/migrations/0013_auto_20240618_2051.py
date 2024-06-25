# Generated by Django 2.2.24 on 2024-06-18 17:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0012_auto_20240514_1822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='evolution',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='previous_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='next_evolution', to='pokemon_entities.Pokemon', verbose_name='Предыдущая эволюция'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение покемона'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название покемона'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_en',
            field=models.CharField(blank=True, max_length=200, verbose_name='Название на английском'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_jp',
            field=models.CharField(blank=True, max_length=200, verbose_name='Название на японском'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='Defence',
            field=models.IntegerField(db_index=True, null=True, verbose_name='Защита'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='Health',
            field=models.IntegerField(db_index=True, null=True, verbose_name='Здоровье'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='Level',
            field=models.IntegerField(db_index=True, null=True, verbose_name='Уровень'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='Stamina',
            field=models.IntegerField(db_index=True, null=True, verbose_name='Выносливость'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='Strength',
            field=models.IntegerField(db_index=True, null=True, verbose_name='Сила'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 18, 20, 51, 13, 586668), verbose_name='Дата и время появления'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 18, 20, 51, 13, 586668), verbose_name='Дата и время исчезновения'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='latitude',
            field=models.FloatField(max_length=200, verbose_name='Широта дислокации покемона'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='longitude',
            field=models.FloatField(max_length=200, verbose_name='Долгота дислокации покемона'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.Pokemon', verbose_name='Ссылка на покемона'),
        ),
    ]
