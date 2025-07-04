from rest_framework import generics, permissions
from .models import Character
from .serializers import CharacterSerializer
from .filters import CharacterFilter
from .permissions import IsAdminOrReadOnly
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
# from applications.commons.response import CustomResponse

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
    
    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     page = self.paginate_queryset(queryset)

    #     if page is not None:
    #         serialized = self.get_serializer(page, many=True)
    #         return self.get_paginated_response({
    #             "codigo": "PEOPLE_PAGINATED",
    #             "mensaje": "Lista paginada de personajes",
    #             "respuesta": serialized.data
    #         })

    #     serialized = self.get_serializer(queryset, many=True)
    #     return CustomResponse.success(
    #         data=serialized.data,
    #         codigo="PEOPLE_LIST_OK",
    #         mensaje="Personajes obtenidos correctamente"
    #     )

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

    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     page = self.paginate_queryset(queryset)

    #     if page is not None:
    #         serialized = self.get_serializer(page, many=True)
    #         return self.get_paginated_response({
    #             "codigo": "CHARACTER_SEARCH_OK",
    #             "mensaje": "Resultados paginados de la búsqueda",
    #             "respuesta": serialized.data
    #         })

    #     serialized = self.get_serializer(queryset, many=True)
    #     return CustomResponse.success(
    #         data=serialized.data,
    #         codigo="CHARACTER_SEARCH_OK",
    #         mensaje="Búsqueda realizada correctamente"
    #     )