
from django.shortcuts import render, redirect, reverse, get_object_or_404

from django.contrib import messages

from products.models import Product

# Create your views here.


def bag(request):
    """view that shows the shopping cart"""
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """Add items to shopping bag"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request,
                            (f'Updated {product.name} '
                            f'quantity to {bag[item_id]}'))
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)