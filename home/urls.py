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
    path('total_expense/', views.total_expense, name='total_expense'),

    path('transactions/', views.transactions, name='transactions'),
    path('transactions_income/', views.transactions_income, name='transactions_income'),
    path('transactions_expense/', views.transactions_expense, name='transactions_expense'),
    path('delete_transaction/<int:id>/', views.delete_transaction, name='delete_transaction'),
    path('update_transaction/<int:id>/', views.update_transaction, name='update_transaction'),

    path('transactions_on_charts/', views.graphic_view, name='transactions_on_charts')

]
