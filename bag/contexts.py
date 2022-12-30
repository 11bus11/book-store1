from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    item_total = 0
    
    

    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += item_data * product.price
        product_count += item_data
        bag_items.append({
            'item_id': item_id,
            'quantity': item_data,
            'product': product,
        })

    if product_count * 0.3 >= 2:
        delivery = 2 * Decimal(settings.DELIVERY_BASE_COST)
    elif product_count * 0.3 >= 6:
        delivery = 3 * Decimal(settings.DELIVERY_BASE_COST)
    else:
        delivery = Decimal(settings.DELIVERY_BASE_COST)

    if total == 0:
        grand_total = total
    else:
        grand_total = delivery + total


    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
