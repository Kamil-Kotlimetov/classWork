from django.urls import path
from .views import products_list

urlpatterns = [
    path('catalog', products_list, name='catalog')
]