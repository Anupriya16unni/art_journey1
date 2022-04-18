from django.shortcuts import render

# Create your views here.

def seller_login (request):
    return render (request,'sellerapp/seller_login.html')

def seller_register (request):
    return render (request,'sellerapp/seller_register.html')