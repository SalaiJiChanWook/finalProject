from django.shortcuts import render
from .models import *
# Create your views here.

def main(request):
    
    product = Product.objects.all().values()
    context = {'product': product,}
        
    return render(request, 'shop/index.html', context)

def about(request):
    
    product2 = Product.objects.all().values()
    context = {'product2': product2,}
    
    
    return render(request, "shop/about.html",context)


def product_detail(request, pk):
	product = Product.objects.get(pk=pk)
	context = {'productDetail': product}
	return render(request, 'shop/productDetail.html', context)


def contact(request):
    product3 = Product.objects.all().values()
    context = {'product3': product3,}
    
    return render(request, "shop/contact.html",context)

def extender(request):
    pds = SubCategory.objects.all().values()
    context = {'pds':pds}
    
    return render(request, "shop/extender.html", context)

def login(request):
    
    
    return render(request, "users/login.html")

def register(request):
    
    
    return render(request, "users/register.html")

def products(request):
    product = Product.objects.all().values()
    product2 = Product.objects.all().values()
    product3 =  Product.objects.all().values()
    context = {'product': product,
               'product2':product2,
               'product3':product3}
    
    return render(request, "shop/products.html",context)

def extender(request):
    
    
    return render(request, "shop/extender.html")