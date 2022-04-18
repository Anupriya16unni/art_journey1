from django.shortcuts import render

# Create your views here.

def addstock (request):
    return render (request,'artistapp/addstock.html')

def register (req):
    return render (req,'artistapp/register.html')

def artist_profile (req):
    return render (req,'artistapp/artist_profile.html')
    
def view_stock (req):
    return render (req,'artistapp/view_stock.html')

def login_security (req):
    return render (req,'artistapp/login_security.html')

def artist_home (req):
    return render (req,'artistapp/artist_home.html')

def artist_login (req):
    return render (req,'artistapp/artist_login.html')

def order_management (req):
    return render (req,'artistapp/order_management.html')

def pending (req):
    return render (req,'artistapp/pending.html')

def processed (req):
    return render (req,'artistapp/processed.html')

