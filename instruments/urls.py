from django.urls import path
from .views import InstrumentList, InstrumentDetail, InstrumentCreate, InstrumentUpdate, InstrumentDelete
from .views import CategoryList, CategoryDetail, CategoryCreate, CategoryUpdate, CategoryDelete
from django.contrib.auth.views import LogoutView

urlpatterns = [
 path('instruments/', InstrumentList.as_view(), name='instruments'),
 path('instrument/<int:pk>/', InstrumentDetail.as_view(), name='instrument'),
 path('instrument-create/', InstrumentCreate.as_view(), name='instrument-create'),
 path('instrument-update/<int:pk>/', InstrumentUpdate.as_view(), name='instrument-update'),
 path('instrument-delete/<int:pk>/', InstrumentDelete.as_view(), name='instrument-delete'),

  path('categories/', CategoryList.as_view(), name='categories'),
 path('category/<int:pk>/', CategoryDetail.as_view(), name='category'),
 path('category-create/', CategoryCreate.as_view(), name='category-create'),
 path('category-update/<int:pk>/', CategoryUpdate.as_view(), name='category-update'),
 path('category-delete/<int:pk>/', CategoryDelete.as_view(), name='category-delete'),

]