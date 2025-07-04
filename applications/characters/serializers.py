from rest_framework import serializers
from .models import Character, Film
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['id', 'title', 'usuario_mod', 'fecha_mod', 'activo']

@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Ejemplo de personaje',
            value={
                "id": 1,
                "name": "Luke Skywalker",
                "height": 172,
                "mass": 77.0,
                "hair_color": "blond",
                "gender": "male",
                "homeworld": "Tatooine",
                "dob": "1977-05-25",
                "films": [],
                "img": "https://starwars-visualguide.com/assets/img/characters/1.jpg",
                "usuario_mod": 1,
                "fecha_mod": "2025-07-04T12:00:00Z",
                "activo": True
            }
        )
    ]
)
class CharacterSerializer(serializers.ModelSerializer):
    films = FilmSerializer(many=True)

    class Meta:
        model = Character
        fields = [
            'id', 'name', 'height', 'mass', 'hair_color', 'gender',
            'homeworld', 'dob', 'films', 'img',
            'usuario_mod', 'fecha_mod', 'activo'
        ]
