import folium
import json

from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime
from .models import Pokemon, PokemonEntity


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons = Pokemon.objects.all()
    now = localtime()
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in pokemons:
        for pokemon_entity in PokemonEntity.objects.filter(pokemon=pokemon, appeared_at__lt=now, disappeared_at__gt=now):
            add_pokemon(
                folium_map, pokemon_entity.latitude,
                pokemon_entity.longitude,
                request.build_absolute_uri(pokemon.image.url)
            )

    
    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': request.build_absolute_uri(pokemon.image.url),
            'title_ru': pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    now = localtime()
    requested_pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    if requested_pokemon.previous_evolution:
        pokemon = {
            'img_url': request.build_absolute_uri(requested_pokemon.image.url),
            'title_ru': requested_pokemon.title,
            'description': requested_pokemon.description,
            'title_en': requested_pokemon.title_en,
            'title_jp': requested_pokemon.title_jp,
            'previous_evolution': {
                'pokemon_id': requested_pokemon.previous_evolution.id,
                'img_url': request.build_absolute_uri(
                    requested_pokemon.previous_evolution.image.url),
                'title_ru': requested_pokemon.previous_evolution.title
            }
        }
    else:
        pokemon = {
            'img_url': request.build_absolute_uri(requested_pokemon.image.url),
            'title_ru': requested_pokemon.title,
            'description': requested_pokemon.description,
            'title_en': requested_pokemon.title_en,
            'title_jp': requested_pokemon.title_jp,
        }
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in PokemonEntity.objects.filter(pokemon=requested_pokemon,
                                                       appeared_at__lt=now,
                                                       disappeared_at__gt=now):
        add_pokemon(
            folium_map, pokemon_entity.latitude,
            pokemon_entity.longitude,
            request.build_absolute_uri(requested_pokemon.image.url)
        )
    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon
    })
