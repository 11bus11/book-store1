from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    fields = ('name', 'email', 'message',)

    list_display = ('name', 'email', 'message',)

    ordering = ('-id',)


admin.site.register(Message, MessageAdmin)
