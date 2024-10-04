from django.db.models import Sum
import random

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
     
    