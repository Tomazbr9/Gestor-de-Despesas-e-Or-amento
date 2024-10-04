from django.shortcuts import render
from utils import graphics

def index(request):
    graphics.graphic_pizza_expense_income()
    graphics.graphic_pizza_category()
    return render(request, 'index.html')



