from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Categorias(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    pontos = models.IntegerField(blank=False, null=False)
    publicado = models.BooleanField(default='True')

    def __str__(self):
        return f'Categoria {self.nome}'

class Campeonatos(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    categoria = models.ForeignKey(
        to=Categorias,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='categoria'
    )
    nivel = models.IntegerField(null=False, blank=False)
    publicado = models.BooleanField(default='True')

    def __str__(self):
        return f'Campeonato {self.nome}'

class Times(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    local = models.CharField(max_length=100, null=False, blank=False)
    historia = models.TextField(null=False, blank=False)
    escudo = models.ImageField(upload_to='foto/%Y/%m/%d', blank=False, null=False)
    titulos = models.ManyToManyField(
        to=Campeonatos,
        related_name='titulos'
    )
    data_registro = models.DateTimeField(default=datetime.now, blank='')
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='usuario'
    )
    publicado = models.BooleanField(default='True')

    def __str__(self):
        return f'Time {self.nome}'