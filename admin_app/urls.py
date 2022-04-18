from django.urls import path
from .import views

urlpatterns =[

    path('message',views.message,name="message"),
    path('reply',views.reply,name="reply"),
    path('admin_manage',views.admin_manange,name="admin_manage"),
    path('admin_profile',views.admin_profile,name="admin_profile"),
    path('admin_logout',views.admin_logout,name="admin_logout")


    
]