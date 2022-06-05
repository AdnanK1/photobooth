from django.urls import path
from . import views

urlpatterns=[
    path('login/',views.login_page,name='login'),
    path('register/',views.register,name='register'),
    path('logout',views.logoutUser,name='logout'),
    path('',views.home,name='home'),
    
]