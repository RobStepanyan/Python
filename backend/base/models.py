from django.db import models
from django.utils import timezone


class Item(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(default=timezone.now)
