from django.db import models
from enums.status import STATUS

class Figma(models.Model):
    RESPONSIVO = (('SIM', 'SIM'),('NAO', 'NAO'),)
    
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=450)
    link_figma = models.URLField()
    mobile = models.CharField(max_length=3, choices=RESPONSIVO, blank=False, null=False,default='NAO')
    status = models.CharField(max_length=1, choices=STATUS, blank=False, null=False, default='P')

    def __str__(self):
        return self.nome

    class  Meta: 
        verbose_name_plural  =  "Projetos no Figma"
