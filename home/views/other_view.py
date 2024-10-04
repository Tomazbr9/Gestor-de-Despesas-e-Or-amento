from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum
from home.models import Category

def income_category(request):
    # obtem todos as categorias do tipo receita
    category = Category.objects.filter(category_type='income').values('id', 'name', 'icone')
    # retorna uma resposta JSON
    return JsonResponse(list(category), safe=False)

def expense_category(request):
    # obtem todos as categorias do tipo despesa
    category = Category.objects.filter(category_type='expense').values('id', 'name', 'icone')
    # retorna uma resposta JSON
    return JsonResponse(list(category), safe=False)

def total_balance(request):
    # obtem os valores totais referentes as categorias
    totals = Category.objects.annotate(
        total_amount=Sum('transaction__amount')).values('name', 'total_amount')
    # retorna uma resposta JSON
    return JsonResponse(list(totals), safe=False)

def total_income(request):
    # obtem os valores totais referentes as categorias do tipo receitas
    totals = Category.objects.filter(category_type='income').annotate(
        total_amount=Sum('transaction__amount')).values('name', 'total_amount')
    
    return JsonResponse(list(totals), safe=False)

def total_expense(request):
    # obtem os valores totais referentes as categorias do tipo despesas
    totals = Category.objects.filter(category_type='expense').annotate(
        total_amount=Sum('transaction__amount')).values('name', 'total_amount')
    
    return JsonResponse(list(totals), safe=False)