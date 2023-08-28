from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from django.contrib.auth.models import User
from order.models import Bucket, ProductBucket

def product_page(request,product_id):
    context = {}
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product
    }
   
    return render(request,'product/product.html',context)



@login_required
def add_to_bucket(request,product_id):
    context = {}
    if request.method == 'POST':
        user = request.user
        
        bucket = Bucket.objects.create(user=user)
        context = {
            'user': user,
            'bucket': bucket
        }

        
       
    return render(request,'product/product.html',context)
    
   

    

        

       




def catalog_page(request):
    context = {}
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request,'product/catalog.html',context)