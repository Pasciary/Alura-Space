from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia



def index(request):
    fotografias = Fotografia.objects.order_by("data_reg").filter(publicada=True)
    
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk= foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})


def buscar(request):
    fotografias = Fotografia.objects.order_by("data_reg").filter(publicada=True)

    if "buscar" in request.GET:
        nome = request.GET['buscar']
        if nome:
            # filtra todos os objetos que buscamos para o que conter o que digitar
            fotografias = fotografias.filter(nome__icontains=nome) 

    return render(request, "galeria/buscar.html", {"cards": fotografias})