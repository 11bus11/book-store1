from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    fields = ('name', 'email', 'message',)

    list_display = ('date', 'name', 'email', 'message',)

    ordering = ('-date',)


admin.site.register(Contact, ContactAdmin)