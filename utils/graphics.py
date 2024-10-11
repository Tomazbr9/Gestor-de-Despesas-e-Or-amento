from utils import for_views
from django.db.models import Sum
from home.models import Category
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT_FOLDER = Path(__file__).parent.parent

def graphic_pizza_expense_income():
    
    total_expense = for_views.total_values(Category, 'expense')

    total_income = for_views.total_values(Category, 'income')
     
    expense_income = ['Despesas', 'Receitas']
    values = [total_expense, total_income]
    colors = ['red', 'green']
    plt.pie(values, labels=expense_income, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.savefig(ROOT_FOLDER / 'base_static' / 'imgs' / 'graphics' / 'expense_income.png')
    plt.close()

def graphic_pizza_category():
    category_values = Category.objects.annotate(
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

    colors = [for_views.generate_random_colors() for _ in name_category]
    plt.pie(
        amount_category, labels=name_category, colors=colors, autopct='%1.1f%%', startangle=140) # type: ignore

    plt.savefig(ROOT_FOLDER / 'base_static' / 'imgs' / 'graphics' / 'graphic_category.png')
    plt.close()

