from django.db import models
from django.db import models
from django.contrib.auth.models import User

class BankAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    balance = models.DecimalField(max_digits=10, decimal_places=2)


class Transaction(models.Model):
    TYPE = [
        ('receita', 'Receita'),
        ('despesa', 'Despesa')
    ]
    bank_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=20)
    type = models.CharField(max_length=7, choices=TYPE)

    def __str__(self):
        return self.description


class Loan(models.Model):
    bank_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    due_date = models.DateField()

class Investment(models.Model):
    bank_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=100)

    rentabilidade = models.DecimalField(max_digits=5, decimal_places=2)
    data_investimento = models.DateField()

    def __str__(self):
        return self.name

class FixedExpense(models.Model):
    bank_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=200)


    

    

class Bitcoin(models.Model):
    valor_compra = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.DecimalField(max_digits=10, decimal_places=8)
    data_compra = models.DateField()



