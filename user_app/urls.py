from unicodedata import name
from django.urls import path
from .import views

urlpatterns =[

    # path('index',views.index,name="index"),
    path('contact',views.contact,name="contact"),
    path('login',views.login,name="login"),
    path('signup',views.signup,name="signup"),
    path('about',views.about,name="about"),
    # path('uhome',views.uhome,name="uhome"),
    path('',views.home,name="home"),
    path('drawing',views.drawing,name="drawing"),
    path('user_profile',views.user_profile,name="user_profile"),
    path('user_login_security',views.user_login_security,name="user_login_security"),
    path('user_address',views.user_address,name="user_address")
    
]