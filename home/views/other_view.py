from django.shortcuts import render
from django.http import JsonResponse
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


