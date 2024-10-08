from django.shortcuts import render
from datetime import datetime


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
    
    context = {
        'view': 'transactions',
        'month': month,
        'year': year,
        'name_month': current_month
    }
    return render(request, 'transactions.html', context)