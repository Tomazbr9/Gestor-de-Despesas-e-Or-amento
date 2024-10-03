from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('expense_category/', views.expense_category, name='expense_category'),
    path('income_category/', views.income_category, name='income_category'),

    # Urls de despesas e receitas
    path('add_transaction/', views.add_transaction, name='add_transaction')

]
