from django import forms
from .models import Livre

class LivreForm(forms.ModelForm):

    class Meta:
        model = Livre
        fields = ['titre', 'auteur', 'datePublication', 'image', 'note', 'commentaire']