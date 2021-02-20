from django.urls import path

from SearchPigeon.views import ARPCD, BRPFC, BRPOA

urlpatterns=[
    path('ARPCD', ARPCD, name='ARPCD'),
    path('BRPFC', BRPFC, name='BRPFC'),
    path('BRPOA', BRPOA, name='BRPOA'),
]