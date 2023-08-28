from django.shortcuts import render,get_object_or_404

from .models import Product

# Create your views here.
def create_order(request):
    context = {}
    
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'order/create_order.html',context)


def cart_page(request):
    return render(request,'order/cart.html')