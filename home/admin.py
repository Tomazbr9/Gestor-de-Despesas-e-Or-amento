from django.contrib import admin
from .models import Revenues, Expenses, Category

@admin.register(Revenues)
class RevenuesAdmin(admin.ModelAdmin):
    list_display = ('value', 'description', 'date')

@admin.register(Expenses)
class ExpensesAdmin(admin.ModelAdmin):
    list_display = ('value', 'description', 'date')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icone')