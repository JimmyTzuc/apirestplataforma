from enum import auto
from django.db import models

# Create your models here.
class RoomModel(models.Model):
    capacity = models.IntegerField()
    date = models.DateTimeField( auto_now=False, auto_now_add=False)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)