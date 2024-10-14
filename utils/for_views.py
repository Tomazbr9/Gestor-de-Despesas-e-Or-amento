from django.db.models import Sum
from home.models import Transaction
from datetime import datetime
from django.shortcuts import render
from django.core.paginator import Paginator
from pathlib import Path
import random
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT_FOLDER = Path(__file__).parent.parent

def total_values(db, type):
    total_value = db.objects.filter(category_type=type).annotate(
        total_amount=Sum('transaction__amount')
    ).values('total_amount')

    total_value = list(total_value)
    total = 0
    for i in total_value:
        value = i.get('total_amount')
        if value is None:
            continue
        
        total += float(value)
    
    total = -(+total) if total < 0 else total
    
    return total


def generate_random_colors():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def sum_values(month, year, type_transactions=None):

    if type_transactions is None:
        total_amount_transactions = Transaction.objects.filter(
            date__month=month, date__year=year
        ).annotate(total_amount=Sum('amount')).values('total_amount')
    else:
        total_amount_transactions = Transaction.objects.filter(
            date__month=month, date__year=year, category__category_type=type_transactions
        ).annotate(total_amount=Sum('amount')).values('total_amount')
        
    total = 0
    for i in list(total_amount_transactions):
        total += float(i['total_amount'])
    
    value_total = f'R$ {total:.2f}'
    return value_total.replace('.', ',').replace('-', '')

def filter_transactions_by_month(request, type_transactions):
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
    
    if type_transactions is None:
        transactions = Transaction.objects.filter(
            date__month=month, date__year=year
        )
    else:
        transactions = Transaction.objects.filter(
            date__month=month, date__year=year, category__category_type=type_transactions)
    
    information_transactions = {
        'month': month,
        'year': year,
        'transactions': transactions,
        'current_month': current_month
    }

    return information_transactions


def filter_transactions(request, type_transactions, action):

    information_transactions = filter_transactions_by_month(
        request, type_transactions)
    
    month = information_transactions['month']
    year = information_transactions['year']
    transactions = information_transactions['transactions']
    current_month = information_transactions['current_month']

    monthhly_balance = sum_values(month, year, type_transactions)
     
    paginator = Paginator(transactions, 10)
    page_number = request.GET.get('page')

    page_transactions = paginator.get_page(page_number)
    
    context = {
        'action': action,
        'monthhly_balance': monthhly_balance,
        'page_obj': page_transactions,
        'view': 'transactions',
        'month': month,
        'year': year,
        'name_month': current_month
    }
    return render(request, 'transactions.html', context)

def filter_type_category_graphic(db, type_category, name_img):
    category_values = db.objects.filter(category_type=type_category).annotate(
        total_amount=Sum('transaction__amount')).values('name', 'total_amount')
    
    category_values = list(category_values)

    name_category = [i.get('name') for i in category_values if i.get('total_amount') is not None]

    amount_category = []
    for i in category_values:
        value = i.get('total_amount')

        if value is None:
            continue

        value = float(value)
        new_value = -(+value) if value < 0 else value
        amount_category.append(new_value)

    colors = [generate_random_colors() for _ in name_category]
    plt.pie(
        amount_category, labels=name_category, colors=colors, autopct='%1.1f%%', startangle=140) # type: ignore

    plt.savefig(ROOT_FOLDER / 'base_static' / 'imgs' / 'graphics' / f'{name_img}.png')
    plt.close()
