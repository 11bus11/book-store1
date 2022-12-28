
from django.shortcuts import render

# Create your views here.


def bag(request):
    """view that shows the shopping cart"""
    return render(request, 'bag/bag.html')

