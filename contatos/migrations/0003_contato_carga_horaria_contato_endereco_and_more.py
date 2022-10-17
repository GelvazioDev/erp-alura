# Generated by Django 4.1.2 on 2022-10-13 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0002_alter_contato_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='carga_horaria',
            field=models.CharField(choices=[('0', '---'), ('1', '4 horas'), ('2', '6 horas'), ('3', '8 horas')], default='0', max_length=20),
        ),
        migrations.AddField(
            model_name='contato',
            name='endereco',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contato',
            name='telefone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]