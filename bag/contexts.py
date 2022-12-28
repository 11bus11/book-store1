from decimal import Decimal
from django.conf import settings


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0

    if product_count * 0.3 >= 2:
        delivery = 2 * Decimal(settings.DELIVERY_BASE_COST / 100)
    if product_count * 0.3 >= 6:
        delivery = 3 * Decimal(settings.DELIVERY_BASE_COST / 100)
    else:
        delivery = Decimal(settings.DELIVERY_BASE_COST / 100)

    grand_total = delivery + total
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context