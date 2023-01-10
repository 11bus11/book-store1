from django.shortcuts import render, redirect, reverse, get_object_or_404
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


def message_view(request):
    """view that returns index page"""

    message = Message.objects.all()
    form = MessageForm()
    template = 'home/messages.html'
    context = {
        'form': form,
        'message': message,
    }

    return render(request, template, context)


def send_message(request):
    """ Send message to store owner (admin) """
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save()
            messages.success(request, 'Successfully sent message!')
        else:
            messages.error(request,
                           ('Failed to send message. '
                            'Please ensure the form is valid.'))
    else:
        form = MessageForm()

    return redirect(reverse('home'))
