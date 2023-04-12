from django.shortcuts import render

def index(request):
    return render(request, "listas/index.html")

def listas(request, listas_id):
    listas = listas.objects.get(id=listas_id)
    return render(request, "listas/listas.html", {
        "listas": listas
    })