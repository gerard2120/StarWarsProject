import django_filters
from .models import Character

class CharacterFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    homeworld = django_filters.CharFilter(lookup_expr='icontains')
    gender = django_filters.CharFilter(lookup_expr='iexact')
    hair_color = django_filters.CharFilter(field_name='hair_color', lookup_expr='icontains')

    class Meta:
        model = Character
        fields = ['name', 'homeworld', 'gender', 'hair_color']
