from django.db import models
from instrutores.models import Instrutor

class Setup(models.Model):
    SIM_NAO = (('SIM', 'SIM'),('NAO', 'NAO'),)
    instrutor = models.ForeignKey(Instrutor, on_delete=models.CASCADE)
    possui_notebook_da_empresa = models.CharField(max_length=3, choices=SIM_NAO, blank=False, null=False,default='NAO')
    notebook = models.CharField(max_length=100)
    tipo_de_camera = models.CharField(max_length=100)
    tipo_de_microfone = models.CharField(max_length=100)
    iluminacao = models.TextField(max_length=450)

    class  Meta: 
        verbose_name_plural  =  "Setup e equipamentos"
