"""mobileproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from .views import index,list_mobiles,add_product,mobile_detail,update,mobile_delete,registration,login_user,\
    signout,item_order,view_my_orders,order_cancel,add_to_cart,view_my_cart,delete_cart_item,cart_order

urlpatterns = [
    # path("",lambda request:render(request,"mobile/base.html")),
    path("",index,name="index"),
    path("mobiles",list_mobiles,name="listmobile"),
    path("addproduct",add_product,name="addproduct"),
    path("mobiles/<int:id>",mobile_detail,name="detail"),
    path("mobiles/update/<int:id>",update,name="update"),
    path("mobiles/delete/<int:id>",mobile_delete,name="delete"),
    path("registration",registration,name="register"),
    path("login",login_user,name="userlogin"),
    path("logout",signout,name="signout"),
    path("ordered/<int:id>",item_order,name="order"),
    path("vieworder",view_my_orders,name="vieworder"),
    path("cancel/<int:id>",order_cancel,name="cancel"),
    path('cart/<int:id>',add_to_cart,name='cart'),
    path("viewcart",view_my_cart,name="viewcart"),
    path("deletecart/<int:id>",delete_cart_item,name="deletecart"),
    path("cartorder/<int:id>",cart_order,name="cartorder"),
]
