from django.db import models

class Figma(models.Model):
    RESPONSIVO = (('SIM', 'SIM'),('NAO', 'NAO'),)
    
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=450)
    link_figma = models.URLField()
    mobile = models.CharField(max_length=3, choices=RESPONSIVO, blank=False, null=False,default='NAO')

    def __str__(self):
        return self.nome
