from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render,redirect
from backend.forms import LivreForm
# Create your views here.

def Accueil(request):
    return render(request,'Accueil.html')

def Services(request):
    return render(request,'Nos_services.html')

def ajouter_livre(request):
    if request.method == 'POST':
        # Si le formulaire est soumis
        form = LivreForm(request.POST, request.FILES)
        if form.is_valid():
            # Si les données du formulaire sont valides, enregistrez le livre
            form.save()
            return redirect('accueil')  # Redirigez vers une vue appropriée après l'ajout du livre (mettere nom de la vue et non URL)
    else:
        # Si c'est une requête GET, créez une nouvelle instance du formulaire
        form = LivreForm()
    
    return render(request, 'Nos_services.html', {'form': form})