from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'name',
        'email',
        'country',
    )

    ordering = (
        'user',
    )


admin.site.register(UserProfile, UserProfileAdmin)
