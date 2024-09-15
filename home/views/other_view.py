from django.http import JsonResponse
from home.models import Category

def category(request):
    # obtem todos os registros da tabela Category
    category = Category.objects.all().values('id', 'name', 'icone')
    # retorna uma resposta JSON
    return JsonResponse(list(category), safe=False)
