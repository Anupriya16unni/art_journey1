from django.shortcuts import render

# Create your views here.
def message (request):
    return render (request,'adminapp/message.html')

def reply (request):
    return render (request,'adminapp/reply.html')

def admin_manange (request):
    return render (request,'adminapp/admin_manage.html')

def admin_profile (request):
    return render (request,'adminapp/admin_profile.html')

def admin_logout (request):
    return render (request,'adminapp/admin_logout.html')