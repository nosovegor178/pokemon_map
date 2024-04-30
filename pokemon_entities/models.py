from django.db import models
import datetime  # noqa F401

# your models here


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f'{self.title}'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    
    latitude = models.FloatField(max_length=200)
    longitude = models.FloatField(max_length=200)

    appeared_at = models.DateTimeField(default=datetime.datetime.now())
    disappeared_at = models.DateTimeField(default=datetime.datetime.now())

    Level = models.IntegerField(db_index=True, null=True)
    Health = models.IntegerField(db_index=True, null=True)
    Strength = models.IntegerField(db_index=True, null=True)
    Defence = models.IntegerField(db_index=True, null=True)
    Stamina = models.IntegerField(db_index=True, null=True)