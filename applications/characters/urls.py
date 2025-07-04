from django.urls import path
from .views import PeopleListView, SearchCharacterView

urlpatterns = [
    path('people', PeopleListView.as_view(), name='people-list'),
    path('search/', SearchCharacterView.as_view(), name='search-character'),
]
