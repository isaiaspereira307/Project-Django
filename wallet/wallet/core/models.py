from django.db import models


class Investimento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    valor_investido = models.DecimalField(max_digits=10, decimal_places=2)
    rentabilidade = models.DecimalField(max_digits=5, decimal_places=2)
    data_investimento = models.DateField()

    def __str__(self):
        return self.nome
    

class Transacao(models.Model):
    TIPO_CHOICES = [
        ('receita', 'Receita'),
        ('despesa', 'Despesa')
    ]
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=7, choices=TIPO_CHOICES)
    data_transacao = models.DateField()

    def __str__(self):
        return self.descricao
    

class Bitcoin(models.Model):
    valor_compra = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.DecimalField(max_digits=10, decimal_places=8)
    data_compra = models.DateField()



