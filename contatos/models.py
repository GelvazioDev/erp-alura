from django.db import models

class Contato(models.Model):
    TIPOS_DE_CARGOS = (('0', '---'),('1', 'Scuba'),('2', 'Instrutor Jr'),('3', 'Instrutor'),('4', 'Web writing'),('5', 'Didática'),('6', 'Designer'),('7', 'Editor'),('8', 'Produção'),('9', 'Scrum Master'),('10', 'Product Owner'),('11', 'Tech Lead'),('12', 'Madrinha/Padrinho'))
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    cargo = models.CharField(max_length=20, choices=TIPOS_DE_CARGOS, blank=False, null=False,default='0')
    # telefone 
    # endereco
    # carga horaria


    def __str__(self):
        return self.nome

    class  Meta: 
        verbose_name_plural  =  "Contatos, e-mail e cargos"
