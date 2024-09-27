from django.db import models

class Revenues(models.Model):
    value = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self) -> str:
        return 'Receita'

class Expenses(models.Model):
    value = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self) -> str:
        return 'Despesa'

class Category(models.Model):
    name = models.CharField(max_length=50)
    icone = models.CharField(max_length=50)

    def __str__(self) -> str:
        return 'Categoria'