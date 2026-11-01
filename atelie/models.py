from django.db import models

class Pedido(models.Model):
    cliente = models.CharField(max_length=100)
    peca = models.CharField(max_length=100)
    data_entrega = models.DateField()
    status = models.CharField(max_length=20, default='Pendente')

class InsumoCalculado(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    metros_fio = models.DecimalField(max_digits=6, decimal_places=2)
    valor_hora = models.DecimalField(max_digits=6, decimal_places=2)
    custo_total = models.DecimalField(max_digits=8, decimal_places=2)
    