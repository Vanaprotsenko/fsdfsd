from django.shortcuts import render

from .models import Product

def product_page(request):
    return render(request,'product/product.html')

def catalog_page(request):
    context = {}
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request,'product/catalog.html',context)