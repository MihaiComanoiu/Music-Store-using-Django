from django.urls import path

from .views import HomeView, AccountView, CustomLoginView, RegisterPage, AdminView
from django.contrib.auth.views import LogoutView

urlpatterns = [
 path('login/', CustomLoginView.as_view(), name='login'),
 path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
 path('register/', RegisterPage.as_view(), name='register'),
 path('', HomeView.as_view(), name='home'),
 path('account/', AccountView.as_view(), name='account'),
 path('managesite/', AdminView.as_view(), name='manage-site'),
]