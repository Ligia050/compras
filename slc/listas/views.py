from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    return render(request, "listas/index.html", {
        "listas": Listas.objects.all()
    })

def listas(request, id):
    listas = Listas.objects.get(id=id)
    itens = Itens.objects.all()

    return render(request, "listas/listas.html", {
        "listas": listas,
        "itens": itens
    })

