from django.contrib import admin
from .models import Category, Transaction

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icone')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('amount', 'description', 'date', 'category')
    ordering = '-id',