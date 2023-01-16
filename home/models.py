from django.db import models
from django.conf import settings


class Message(models.Model):
    class Meta:
        verbose_name_plural = 'Messages'

    name = models.CharField(max_length=254, null=True, blank=True)
    email = models.EmailField(max_length=254)
    message = models.TextField()

    def __name__(self):
        return self.name
