from django.db import models

class Ideia(models.Model):
    ideia_em_poucas_palavras = models.CharField(max_length=20)
    detalhes = models.TextField(max_length=500)

    def __str__(self):
        return self.tituideia_em_poucas_palavras

    class  Meta: 
        verbose_name_plural  =  "Tem uma ideia? Que tal anotar!"
