
from django.urls import path
from . import views
urlpatterns = [
   path('Accueil/',views.Accueil,name='accueil'),
   path('Services/',views.ajouter_livre,name='services')
]
