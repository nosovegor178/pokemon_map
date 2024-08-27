from django.db import models
import datetime  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200,
                             verbose_name='Название покемона')
    title_en = models.CharField(max_length=200,
                                blank=True,
                                verbose_name='Название на английском')
    title_jp = models.CharField(max_length=200, 
                                blank=True,
                                verbose_name='Название на японском')
    image = models.ImageField(blank=True,
                              null=True,
                              verbose_name='Изображение покемона')
    description = models.TextField(blank=True,
                                   null=True,
                                   verbose_name='Описание')
    previous_evolution = models.ForeignKey("self",
                                  on_delete=models.CASCADE,
                                  blank=True,
                                  null=True,
                                  related_name='next_evolutions',
                                  verbose_name='Предыдущая эволюция')


    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon,
                                on_delete=models.CASCADE,
                                related_name='entities',
                                verbose_name='Ссылка на покемона')
    latitude = models.FloatField(verbose_name='Широта дислокации покемона')
    longitude = models.FloatField(verbose_name='Долгота дислокации покемона')
    appeared_at = models.DateTimeField(verbose_name='Время и датапоявления покемона')
    disappeared_at = models.DateTimeField(verbose_name='Время и дата исчезновения покемона')
    level = models.IntegerField(db_index=True,
                                null=True,
                                verbose_name='Уровень')
    health = models.IntegerField(db_index=True,
                                 null=True,
                                 verbose_name='Здоровье')
    strength = models.IntegerField(db_index=True,
                                   null=True,
                                   verbose_name='Сила')
    defence = models.IntegerField(db_index=True,
                                  null=True,
                                  verbose_name='Защита')
    stamina = models.IntegerField(db_index=True,
                                  null=True,
                                  verbose_name='Выносливость')
    
    def __str__(self):
        return self.pokemon