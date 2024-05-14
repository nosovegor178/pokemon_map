from django.db import models
import datetime  # noqa F401

# your models here


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
    description = models.CharField(max_length=1000,
                                   blank=True,
                                   null=True,
                                   verbose_name='Описание')
    evolution = models.ForeignKey("self",
                                  on_delete=models.CASCADE,
                                  blank=True,
                                  null=True,
                                  related_name='next',
                                  verbose_name='Эволюции покемона')

    def __str__(self):
        return f'{self.title}'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon,
                                on_delete=models.CASCADE,
                                verbose_name='Ссылка на покемона')
    
    latitude = models.FloatField(max_length=200,
                                 verbose_name='Широта дислокации покемона')
    longitude = models.FloatField(max_length=200,
                                  verbose_name='Долгота дислокации покемона')

    appeared_at = models.DateTimeField(default=datetime.datetime.now(),
                                       verbose_name='Дата и время появления')
    disappeared_at = models.DateTimeField(default=datetime.datetime.now(),
                                          verbose_name='Дата и время исчезновения')

    Level = models.IntegerField(db_index=True,
                                null=True,
                                verbose_name='Уровень')
    Health = models.IntegerField(db_index=True,
                                 null=True,
                                 verbose_name='Здоровье')
    Strength = models.IntegerField(db_index=True,
                                   null=True,
                                   verbose_name='Сила')
    Defence = models.IntegerField(db_index=True,
                                  null=True,
                                  verbose_name='Защита')
    Stamina = models.IntegerField(db_index=True,
                                  null=True,
                                  verbose_name='Выносливость')