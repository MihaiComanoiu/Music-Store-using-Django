from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Instrument

class InstrumentList( ListView):
 model = Instrument
 context_object_name = 'instruments'
 template_name = 'instruments/instruments.html'

class InstrumentDetail(DetailView):
 model = Instrument
 context_object_name = 'instrument'
 template_name = 'instruments/instrument.html'

class InstrumentCreate(LoginRequiredMixin, CreateView):
 model = Instrument
 fields = ['name', 'category', 'price', 'description', 'image']
 success_url = reverse_lazy('instruments')
 template_name = 'instruments/instrument-create.html'

class InstrumentUpdate(LoginRequiredMixin, UpdateView):
 model = Instrument
 fields = ['name', 'category', 'price', 'description', 'image']
 success_url = reverse_lazy('instruments')
 template_name = 'instruments/instrument-update.html'

class InstrumentDelete(LoginRequiredMixin, DeleteView):
 model = Instrument
 context_object_name = 'instrument'
 success_url = reverse_lazy('instruments')
 template_name = 'instruments/instrument-delete.html'