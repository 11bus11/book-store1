from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    fields = ('date', 'name', 'email', 'message',)

    list_display = ('date', 'name', 'email', 'message',)

    ordering = ('-date',)


admin.site.register(Message, MessageAdmin)
