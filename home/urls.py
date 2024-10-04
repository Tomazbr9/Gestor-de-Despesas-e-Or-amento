from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),

    # Urls de Tipos de Categorias
    path('expense_category/', views.expense_category, name='expense_category'),
    path('income_category/', views.income_category, name='income_category'),

    # Urls de despesas e receitas
    path('add_transaction/', views.add_transaction, name='add_transaction'),
    path('total_balance/', views.total_balance, name='total_balance'),
    path('total_income/', views.total_income, name='total_income'),
    path('total_expense/', views.total_expense, name='total_expense')
]
