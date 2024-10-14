from django.shortcuts import render
from utils import graphics

def index(request):
    graphics.graphic_pizza_expense_income()
    graphics.graphic_pizza_category()
    graphics.graphic_expense_category()
    graphics.graphic_income_category()
    context = {
        'view': 'index'
    }
    return render(request, 'index.html', context)



