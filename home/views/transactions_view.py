from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from datetime import datetime
from django.urls import reverse
from django.db.models import Sum
from ..models import Transaction, Category
from utils.for_views import sum_values, filter_transactions

def transactions(request):

    action = reverse('home:transactions')

    transactions = filter_transactions(request, None, action)
    return transactions

# Deleta as Transação clicada
def delete_transaction(requestm, id):
    transaction = get_object_or_404(Transaction, id=id)

    transaction.delete()

    return redirect('home:transactions')


# Atualiza as Transações
def update_transaction(request, id):
    
    transaction = get_object_or_404(Transaction, id=id)

    if request.method == 'POST':
        category_id = request.POST.get('id')
        value = request.POST.get('value')
        amount = float(value.replace('R$', '').replace(' ', ''))
        description = request.POST.get('description')
        date = request.POST.get('date')

        category = Category.objects.get(id=category_id)
        
        if category.category_type == 'expense':
                amount = -amount
        
        transaction.amount = amount # type: ignore
        transaction.description = description

        if not date:
            date = datetime.now()

        transaction.date = date 
        transaction.category = category

        transaction.save()

        return redirect('home:transactions')

    return render(request, 'transactions.html')

def transactions_income(request):

    action = reverse('home:transactions_income')
    transactions = filter_transactions(request, 'income', action)
    return transactions

def transactions_expense(request):

    action = reverse('home:transactions_expense')
    transactions = filter_transactions(request, 'expense', action)
    return transactions

    
    


