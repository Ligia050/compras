from django.db import models
from django.contrib import admin


class Listas(models.Model):
    nome_lista = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.nome_lista}"

class Itens(models.Model):
    itens = models.CharField(max_length=64)
    preco= models.FloatField()
    nome_lista  = models.ForeignKey(Listas, on_delete=models.CASCADE, related_name="Itens")

    def __str__(self):
        return f"{self.itens} R$ {self.preco} "

