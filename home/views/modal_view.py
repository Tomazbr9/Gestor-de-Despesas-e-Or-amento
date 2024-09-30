from django.http import JsonResponse
from django.shortcuts import render, redirect
from ..models import Category, Transaction


# Parei aqui
def add_transaction(request):
    if request.method == "POST":
        category_id = request.POST.get('id')

        value = request.POST.get('value')
        amount = float(value.replace('R$', '').replace(' ', ''))

        description = request.POST.get('description')
        date = request.POST.get('date')

        if category_id and value:
            category = Category.objects.get(id=category_id)

            if category.category_type == 'expense':
                amount = -amount

            if not date:
                date = None

            transaction = Transaction.objects.create(
                amount = amount,
                description = description,
                date = date,
                category = category,
            )

            transaction.save()
        else:
            JsonResponse({'status': 'error'})
    else:
        JsonResponse({'status': 'method invalid'})
    
    return redirect('home:index')
    

