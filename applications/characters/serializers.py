from rest_framework import serializers
from .models import Character, Film

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['id', 'title', 'usuario_mod', 'fecha_mod', 'activo']


class CharacterSerializer(serializers.ModelSerializer):
    films = FilmSerializer(many=True)

    class Meta:
        model = Character
        fields = [
            'id', 'name', 'height', 'mass', 'hair_color', 'gender',
            'homeworld', 'dob', 'films', 'img',
            'usuario_mod', 'fecha_mod', 'activo'
        ]
