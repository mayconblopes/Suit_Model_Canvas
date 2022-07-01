from django.db import models

# Create your models here.

class SuitModelCanvas (models.Model):
    pretensao = models.CharField(max_length=1000)
    requisitos_documentais = models.CharField(max_length=1000)
    nome_peca = models.CharField(max_length=1000)
    causa_pedir = models.CharField(max_length=1000)
    pedidos = models.CharField(max_length=1000)
    beneficios = models.CharField(max_length=1000)
    partes_processo = models.CharField(max_length=500)
    terceiros = models.CharField(max_length=500)
    competencia = models.CharField(max_length=200)
    equipe = models.CharField(max_length=500)
    provas = models.CharField(max_length=1000)
    entregas_processuais = models.CharField(max_length=1000)
    restricoes = models.CharField(max_length=1000)
    riscos = models.CharField(max_length=1000)
    prazos = models.CharField(max_length=1000)
    honorarios = models.CharField(max_length=500)
    demais_despesas = models.CharField(max_length=1000)
    ementa = models.CharField(max_length=3000)

    
