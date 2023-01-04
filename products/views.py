from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from .models import Product, Category
from .forms import ProductForm


def all_products(request):
    """view that shows products (sorting and search too)"""

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No search criteria was entered!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(language__icontains=query) | Q(author__icontains=query)
            products = products.filter(queries)

    context = {
            'products': products,
            'search_term': query,
            'current_categories': categories,
        }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """view that shows product details for chosen product."""

    product = get_object_or_404(Product, pk=product_id)

    print(product)

    context = {
            'product': product,
        }

    return render(request, 'products/product_detail.html', context)


def add_products(request):
    """ Adding a product to store (admin)"""
    form = ProductForm()
    template = 'products/add_products.html'
    context = {
        'form': form,
    }

    return render(request, template, context)