from email.policy import default
from django.db import models
from instrutores.models import Instrutor
from figma.models import Figma
from django.core.validators import MaxValueValidator, MinValueValidator
from enums.categoria import CATEGORIA_DO_CURSO
from enums.status import STATUS

class Curso(models.Model):
    
    nome = models.CharField(max_length=50)
    id_do_curso = models.IntegerField(default=0000, validators=[MaxValueValidator(99999),MinValueValidator(0000)])
    categoria = models.CharField(max_length=1, choices=CATEGORIA_DO_CURSO, blank=False, null=False, default='0')
    instrutor = models.ForeignKey(Instrutor, on_delete=models.CASCADE)
    projeto = models.ForeignKey(Figma, on_delete=models.CASCADE)
    descricao = models.TextField(max_length=450)
    github = models.URLField()
    status = models.CharField(max_length=1, choices=STATUS, blank=False, null=False, default='P')

    def __str__(self):
        return self.nome

    class  Meta: 
        verbose_name_plural = 'Cursos'
        