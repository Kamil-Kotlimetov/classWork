from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def good_bye(request, *args, **kwargs):
    return HttpResponse(f'Good Bye!')