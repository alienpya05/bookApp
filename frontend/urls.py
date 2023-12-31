
from django.urls import path
from . import views
urlpatterns = [
   path('Accueil/',views.afficher_livre,name='accueil'),
   path('Services/',views.ajouter_livre,name='services'),
   path('livre/<str:livre_titre>/', views.detail_Livre, name='detail_livre'),
]