from django.urls import path

from SearchPigeon.api.views import search_pigeon

urlpatterns = [
    path('search_pigeon/<ring_no>', search_pigeon, name="search_pigeon"),
]