from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from django.views.generic.edit import FormView

from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

class HomeView(TemplateView):
 template_name = 'base/index.html'

class AccountView(TemplateView):
 template_name = 'base/account.html'

class CustomLoginView(LoginView):
 template_name = 'base/login.html'
 fields = '__all__'
 redirect_authenticated_user = True
 
 def get_success_url(self):
  return reverse_lazy('home')

class RegisterPage(FormView):
 template_name = 'base/register.html'
 form_class = UserCreationForm
 redirect_authenticated_user = True
 success_url = reverse_lazy('home')

 def form_valid(self, form):
  user = form.save()
  if user is not None:
   login(self.request, user)
  return super(RegisterPage, self).form_valid(form)

 def get(self, *args, **kwargs):
  if self.request.user.is_authenticated:
   return redirect('home')
  return super(RegisterPage, self).get(*args, **kwargs)

class AdminView(TemplateView):
  template_name = 'base/admin.html'