from django.db import models
from instrutores.models import Instrutor
from enums.categoria import CATEGORIA_DO_CURSO
from django.core.validators import MaxValueValidator, MinValueValidator
from enums.status import STATUS

class Artigo(models.Model):
    titulo = models.CharField(max_length=50)
    categoria = models.CharField(max_length=1, choices=CATEGORIA_DO_CURSO, blank=False, null=False, default='0')
    id_do_artigo = models.IntegerField(default=0000, validators=[MaxValueValidator(99999),MinValueValidator(0000)])
    publico_alvo = models.TextField(max_length=450)
    instrutor = models.ForeignKey(Instrutor, on_delete=models.CASCADE, related_name='instrutor')
    link_doc = models.URLField()
    status = models.CharField(max_length=1, choices=STATUS, blank=False, null=False, default='P')

    def __str__(self):
        return self.titulo

    class Meta: 
        verbose_name_plural  =  "Artigos"