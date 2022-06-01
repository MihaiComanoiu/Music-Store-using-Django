from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from .models import Instrument


# Create your models here.
class Cart(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 instruments = models.ManyToManyField(Instrument)
