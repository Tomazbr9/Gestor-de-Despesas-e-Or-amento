from django.shortcuts import render
from django.urls import reverse

def graphic_view(request):
    
    action = reverse('home:graphic_view')

    


    return render(request, 'monthly_charts.html')