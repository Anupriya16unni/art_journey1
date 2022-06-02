from django.shortcuts import render,redirect

from admin_app.models import AdminLogin
import user_app.models




# Create your views here.
def message (request):
    # current_user=request.session['user_id']
    # contact=user_app.models.ContactUs.objects.get(id=current_user)
    # print(new_user)
    contact=user_app.models.ContactUs.objects.all()
    return render (request,'adminapp/message.html',{'cnt':contact})

def reply (request):
    return render (request,'adminapp/reply.html')

def artist_request (request):
    return render (request,'adminapp/artist_request.html')

def admin_profile (request):
    current_admin=request.session['admin_id']
    profile_name=AdminLogin.objects.get(id=current_admin)
    return render (request,'adminapp/admin_profile.html',{'profile':profile_name})

def admin_logout (request):
    return render (request,'adminapp/admin_logout.html')

def admin_home (request):
    current_admin=request.session['admin_id']
    profile_details=AdminLogin.objects.get(id=current_admin)
    return render (request,'adminapp/admin_home.html',{'profile':profile_details})

def artist_info (request):
    return render (request,'adminapp/artist_info.html')

def customer_info (request):
    return render (request,'adminapp/customer_info.html')

def admin_login (request):
    error=''
    if request.method=='POST':
        admin_name=request.POST['uname']
        admin_pass=request.POST['pass']
        try:
            admin_data=AdminLogin.objects.get(username=admin_name,password=admin_pass)
            request.session['admin_id']=admin_data.id
            return redirect('admin_home')
        except:
            error="invalid username or password"
    return render (request,'adminapp/admin_login.html',{'error':error})