from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('editprofile/', views.editprofile, name='editprofile'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('adminhome/', views.adminhome, name='adminhome'),
    path('addproduct/', views.addproduct, name='addproduct'),
    path('productlist/', views.productlist, name='productlist'),
    path('deleteproduct/<int:id>/', views.deleteproduct, name='deleteproduct'),
    path('editproduct/<int:id>/', views.editproduct, name='editproduct'),
    path('userlist/', views.userlist, name='userlist'),
    path('userproductlist/', views.userproductlist, name='userproductlist'),
    path('addtocart/<int:pdid>/', views.addtocart, name='addtocart'),
    path('usercartlist/', views.usercartlist, name='usercartlist'),
    path('admincartlist/', views.admincartlist, name='admincartlist'),
    path('favourites/', views.favourites, name='favourites'),
    path('addtofavourites/<int:pdid>/', views.addtofavourites, name='addtofavourites'),


    

    
]
