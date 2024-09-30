from django.db import models

class Category(models.Model):

    CATEGORY_TYPES = [
        ('expense', 'Despesa'),
        ('income', 'Receita'),
    ]

    name = models.CharField(max_length=50)
    icone = models.CharField(max_length=100)

    category_type = models.CharField(max_length=7, choices=CATEGORY_TYPES)

    def __str__(self) -> str:
        return self.name

class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255, blank=True)
    date = models.DateField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f'{self.category.name}: {self.amount}'
