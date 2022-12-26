from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from .models import Product, Category
#from .forms import ProductForm


def all_products(request):
    """view that shows products (sorting and search too)"""

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    context = {
            'products': products,
        }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """view that shows product details for chosen product."""

    product = get_object_or_404(Product, pk=product_id)

    context = {
            'product': product,
        }

    return render(request, 'products/product_detail.html', context)

