from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from django.contrib.auth.models import User
from order.models import Bucket, ProductBucket

def product_page(request,product_id):
    context = {}
    product = get_object_or_404(Product, pk=product_id)
    bject_count = Product.objects.count()
    context = {
        'product': product,
        'count': bject_count
    }
   
    return render(request,'product/product.html',context)





@login_required
def add_to_bucket(request,product_id):
    context = {}
    user = request.user
    
    bucket,  create = Bucket.objects.get_or_create(user=user)
    product = Product.objects.get(pk = product_id)
    ProductinBucket = ProductBucket.objects.create(count = 1,product = product, bucket = bucket)
   
    return redirect(f'/products/{product_id}/',context)







def catalog_page(request):
    context = {}
    bject_count = Product.objects.count()

    products = Product.objects.all()
    
    productbucket = ProductBucket.objects.all()
    context = {
        'products': products,
        'productbucket': productbucket,
        'count': bject_count
        
    }
    return render(request,'product/catalog.html',context)




