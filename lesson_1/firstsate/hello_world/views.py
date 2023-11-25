from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello_world(request, *args, **kwargs):
    return HttpResponse(f'Hello world!')