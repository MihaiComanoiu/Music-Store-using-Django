from django.shortcuts import redirect, render
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from .models import Cart


class CartDetail(DetailView):
 model = Cart
 context_object_name = 'cart'
 template_name = 'base/account.html'

