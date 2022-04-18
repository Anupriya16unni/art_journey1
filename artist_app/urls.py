from django.urls import path
from .import views

urlpatterns =[

    path('addstock',views.addstock,name="addstock"),
    path('register',views.register,name="register"),
    path('artist_profile',views.artist_profile,name="artist_profile"),
    path('view_stock',views.view_stock,name="view_stock"),
    path('login_security',views.login_security,name="login_security"),
    path('artist_home',views.artist_home,name="artist_home"),
    path('artist_login',views.artist_login,name="artist_login"),
    path('order_management',views.order_management,name="order_management"),
    path('pending',views.pending,name="pending"),
    path('processed',views.processed,name="processed")


    
]