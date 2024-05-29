from django.db import models
from django.utils import timezone

class Tarefa(models.Model):
    titulo = models.CharField(max_length=50 )
    descricao = models.TextField(max_length=100 )
    data_criacao = models.DateTimeField(default=timezone.now)
