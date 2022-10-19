"""Datatables URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from App import views



urlpatterns = [
   path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('home', views.home, name="home"),

    path('add_product', views.add_product, name="add_product"),

    # ************************* MATCHES **********************
    path('productview', views.productview.as_view(), name="productview"), 
    path('productunmachview', views.productunmachview.as_view(), name="productunmachview"),
    path('deletematch', views.deletematch.as_view(), name="deletematch"),
    path('matchproduct', views.matchproduct, name="matchproduct"),
    path('unmatched', views.unmatched, name="unmatched"),
    path('delmatch', views.delmatch, name="delmatch"),
    path('matchunmach', views.matchunmach, name="matchunmach"),
    path('unmatchunmatch', views.unmatchunmatch, name="unmatchunmatch"),
    path('returnunmaches', views.returnunmaches, name="returnunmaches"),
    path('viewmatch', views.viewmatch, name="viewmatch"),
    
    # **************** vendors **********************
    path('bestbuy', views.bestbuy, name="bestbuy"),
    path('lowes', views.lowes, name="lowes"),
    path('homedepot', views.homedepot, name="homedepot"),
    path('walmart', views.walmart, name="walmart"),

    # **************** product master ****************
    path('bestbuymaster', views.bestbuymaster, name="bestbuymaster"),
    path('lowesmaster', views.lowesmaster, name="lowesmaster"),
    path('homedepotmaster', views.homedepotmaster, name="homedepotmaster"),
  
    # **************** modals vendors ****************
    path('bestbuyview/<str:prod_id>', views.bestbuyview, name="bestbuyview"),
    path('lowesview/<str:prod_id>', views.lowesview, name="lowesview"),
    path('homedepotview/<str:prod_id>', views.homedepotview, name="homedepotview"),
    path('walmartview/<str:prod_id>', views.walmartview, name="walmartview"),

     # **************** modals product master ****************
    path('bestbuymasterview/<str:prod_id>', views.bestbuymasterview, name="bestbuymasterview"),
    path('lowesview/<str:prod_id>', views.lowesview, name="lowesview"),
    path('homedepotmasterview/<str:prod_id>', views.homedepotmasterview, name="homedepotmasterview"),


    path('editviewbestbuy/<str:prod_id>', views.editviewbestbuy, name="editviewbestbuy"),
    path('editbestbuy', views.editbestbuy, name="editbestbuy"),
    path('about', views.about, name="about"),
    path('singledayrun', views.singledayrun, name="singledayrun"),
    path('multidayrun', views.multidayrun, name="multidayrun"),
    path('productlist', views.productlist, name="productlist"),
    
    path('json/', views.multidayrunjson, name="multidayrunjson"),
    path('jsonlowes/', views.lowesjson, name="lowesjson"),
    path('jsonbestbuy/', views.bestbuyjson, name="bestbuyjson"),

     # **************** Carrito ****************
    path('agregar/<int:producto_id>/', views.agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', views.restar_producto, name="Sub"),
    path('limpiar/', views.limpiar_carrito, name="CLS"),

    path('login/', views.Login, name="login"),
    path('login_user', views.LoginUser, name="login_user"),
    path('logout/', views.LogoutUser, name="logout"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
