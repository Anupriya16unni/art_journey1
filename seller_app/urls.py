from django.urls import path
from .import views

urlpatterns =[

    path('seller_login',views.seller_login,name="seller_login"),
    path('seller_register',views.seller_register,name="seller_register")
]