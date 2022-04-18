from django.shortcuts import render

# Create your views here.

# def index (request):
    # return render (request,'userapp/index.html')

def contact (request):
    return render (request,'userapp/contact.html')

def login (request):
    return render (request,'userapp/login.html')

def signup (request):
    return render (request,'userapp/signup.html')

def about (request):
    return render (request,'userapp/about.html')

# def uhome (request):
#     return render (request,'userapp/uhome.html')

def home (request):
    return render (request,'userapp/home.html')

def drawing (request):
    return render (request,'userapp/drawing.html')

def user_profile (request):
    return render (request,'userapp/user_profile.html')

def user_login_security (request):
    return render (request,'userapp/user_login_security.html')

def user_address (request):
    return render (request,'userapp/user_address.html')