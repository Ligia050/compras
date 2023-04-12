from django.db import models

class listas(models.Model):
    nome = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id}: {self.nome}"

