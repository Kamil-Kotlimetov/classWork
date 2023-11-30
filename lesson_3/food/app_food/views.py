from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category

# def products_list(request, *args, **kwargs):
#     if request.method == 'GET':
#         products = Product.objects.all()
#         # print(products)
#         context = {'products': products}
#         return render(request, template_name='app_food/index.html', context=context)

def main(request, *args, **kwargs):
    return render(request, 'app_food/base.html')

def catalog(request, *args, **kwargs):
    categories = Category.objects.all()
    return render(request, 'app_food/index.html', context={'categories': categories})

def category(request, *args, **kwargs):
    products = Product.objects.filter(category__id=kwargs['pk'])
    return render(request, 'app_food/category.html', context={'products': products})