from django.urls import path
from .views import InstrumentList, InstrumentDetail, InstrumentCreate, InstrumentUpdate, InstrumentDelete
from django.contrib.auth.views import LogoutView

urlpatterns = [
 path('instruments/', InstrumentList.as_view(), name='instruments'),
 path('instrument/<int:pk>/', InstrumentDetail.as_view(), name='instrument'),
 path('instrument-create/', InstrumentCreate.as_view(), name='instrument-create'),
 path('instrument-update/<int:pk>/', InstrumentUpdate.as_view(), name='instrument-update'),
 path('instrument-delete/<int:pk>/', InstrumentDelete.as_view(), name='instrument-delete'),

]