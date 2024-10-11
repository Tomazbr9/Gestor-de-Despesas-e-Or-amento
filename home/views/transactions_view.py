from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from datetime import datetime
from ..models import Transaction, Category

def transactions(request):

    months = [
        'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio',
        'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
        'Novembro', 'Dezembro']
    
    if request.method == 'GET':
        month = request.GET.get('month', datetime.now().month)
        year = request.GET.get('year', datetime.now().year)
        direction = request.GET.get('direction')

        month = int(month)
        year = int(year)

        if direction == 'previous':
            if month == 1:
                month = 12
                year -= 1
            else:
                month -= 1
        elif direction == 'next':
            if month == 12:
                month = 1
                year += 1
            else:
                month += 1
        
        current_month = months[month - 1]
    
    transactions = Transaction.objects.filter(
        date__month=month, date__year=year
    )

    paginator = Paginator(transactions, 10)
    page_number = request.GET.get('page')

    page_transactions = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_transactions,
        'view': 'transactions',
        'month': month,
        'year': year,
        'name_month': current_month
    }
    return render(request, 'transactions.html', context)

# Deleta as Transação clicada
def delete_transaction(requestm, id):
    transaction = get_object_or_404(Transaction, id=id)

    transaction.delete()

    return redirect('home:transactions')


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
