from django.shortcuts import render

from products.models import Product, ProductCategory


# Create your views here.
#контролеры = views = функции

def index(request):
    context = {
        'title': 'Store'
    }
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'title': 'Store-Каталог',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),
    }
    return render(request, 'products/products.html', context)

