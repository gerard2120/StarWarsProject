from rest_framework import generics, permissions
from .models import Character
from .serializers import CharacterSerializer
from .filters import CharacterFilter
from .permissions import IsAdminOrReadOnly
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample

@extend_schema(
    description="Lista paginada de personajes de Star Wars.",
    tags=["People"],
    examples=[
        OpenApiExample(
            'Ejemplo de respuesta',
            value={
                "count": 1,
                "results": [
                    {
                        "id": 1,
                        "name": "Luke Skywalker",
                        "height": 172,
                        "mass": 77.0,
                        "hair_color": "blond",
                        "gender": "male",
                        "homeworld": "Tatooine",
                        "dob": "19BBY",
                        "films": [],
                        "img": "https://starwars-visualguide.com/assets/img/characters/1.jpg"
                    }
                ]
            }
        )
    ]
)
class PeopleListView(generics.ListAPIView):
    queryset = Character.objects.all().prefetch_related('films')
    serializer_class = CharacterSerializer
    permission_classes = [IsAdminOrReadOnly]

@extend_schema(
    description="Búsqueda avanzada de personajes por nombre, planeta, género o color de cabello.",
    tags=["People"],
    parameters=[
        OpenApiParameter("name", str, OpenApiParameter.QUERY, description="Nombre del personaje"),
        OpenApiParameter("homeworld", str, OpenApiParameter.QUERY, description="Planeta de origen"),
        OpenApiParameter("gender", str, OpenApiParameter.QUERY, description="Género"),
        OpenApiParameter("hair_color", str, OpenApiParameter.QUERY, description="Color de cabello"),
    ]
)
class SearchCharacterView(generics.ListAPIView):
    queryset = Character.objects.all().prefetch_related('films')
    serializer_class = CharacterSerializer
    filterset_class = CharacterFilter
    permission_classes = [permissions.IsAuthenticated]
