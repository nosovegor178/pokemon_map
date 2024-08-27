# Generated by Django 2.2.24 on 2024-08-13 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0014_auto_20240625_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='previous_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='next_evolutions', to='pokemon_entities.Pokemon', verbose_name='Предыдущая эволюция'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='latitude',
            field=models.FloatField(verbose_name='Широта дислокации покемона'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='longitude',
            field=models.FloatField(verbose_name='Долгота дислокации покемона'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entities', to='pokemon_entities.Pokemon', verbose_name='Ссылка на покемона'),
        ),
    ]