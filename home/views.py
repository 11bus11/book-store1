from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import MessageForm
from .models import Message

# Create your views here.


def index(request):
    """view that returns index page"""

    message_form = MessageForm()
    template = 'home/index.html'
    context = {
        'message_form': message_form,
    }

    return render(request, template, context)


def messages(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save()
            messages.success(request, 'Successfully sent message!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           ('Failed to send message. '
                            'Please ensure the form is valid.'))
    else:
        form = MessageForm()

    template = 'index.html'
    context = {
        'form': form,
    }

    return render(request, template, context)