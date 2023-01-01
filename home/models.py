from django.db import models
from django.conf import settings


class Contact(models.Model):
    name = models.CharField(max_length=254, null=True, blank=True)
    email = models.EmailField(max_length=254)
    message = models.CharField(max_length=3000)
    date = models.DateTimeField(auto_now_add=True, editable=True, blank=True)

    def __name__(self):
        return self.name
