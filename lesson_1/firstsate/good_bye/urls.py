from django.urls import path
from .views import good_bye

urlpatterns = [
    path('', good_bye, name='good_bye')
]