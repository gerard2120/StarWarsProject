from rest_framework import generics, permissions
from .models import Character
from .serializers import CharacterSerializer
from .filters import CharacterFilter

class PeopleListView(generics.ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    filterset_class = CharacterFilter
    permission_classes = [permissions.IsAuthenticated]

class SearchCharacterView(generics.ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    filterset_class = CharacterFilter
    permission_classes = [permissions.IsAuthenticated]
