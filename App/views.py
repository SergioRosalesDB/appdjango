from itertools import product
from pyexpat.errors import messages
import random
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.views.generic import View
from App.Carrito import Carrito
from mi_app_2.models import BbCategoriesImport
from mi_app_2.models import BbDetailsImport
from mi_app_2.models import BbProductImages
from mi_app_2.models import Bestbuymodel
from mi_app_2.models import Databasechangelog
from mi_app_2.models import Databasechangeloglock
from mi_app_2.models import DevopsBestBuy
from mi_app_2.models import Lowesmodel
from mi_app_2.models import Homemodel
from mi_app_2.models import Walmartmodel
from App.models import Productlist
from App.models import Product
from App.models import Deleteproductmatch
from django.views.generic import View
import time
from django.contrib.auth import  authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django import template
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


@login_required(login_url="/login/")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)

# Create your views here.


def home(request):
    return render(request, "home.html")


# ***********  Match ***********

class productview(View):
    def get(self, request):
        allproduct=Product.objects.all()
        context={
            'products':allproduct
        }
        return render(request, 'productmatchedit.html', context)

class productviewdos(View):
    def get(self, request):
        allproduct=Product.objects.all()
        context={
            'products':allproduct
        }
        return render(request, 'productmatcheditdos.html', context)

class productunmachview(View):
    def get(self, request):
        allproduct=Product.objects.all()
        context={
            'products':allproduct
        }
        return render(request, 'productunmatchedit.html', context)

def matchproduct(request):
    if request.method=='POST':
            product_ids=request.POST.getlist('id[]')
            raw_num = random.randrange(0, 10000)
            for id in product_ids:
                product = Product.objects.get(id=id)
                product.matchid = request.POST.get('raw_num', int(raw_num))
                product.save()
            return redirect('productview')   

def unmatched(request):
   if request.method=='POST':
            product_ids=request.POST.getlist('id[]')
            for id in product_ids:
                product = Product.objects.get(id=id)
                product.matchid = request.POST.get('raw_num')
                product.save()
                product.delete()
            return redirect('productview')

def delmatch(request):
    if request.method=='POST':
            product_ids=request.POST.getlist('id[]')
            for id in product_ids:
                product = Product.objects.get(id=id)
                product.delete()
            return redirect('productview')

def viewmatch(request):
    if request.method=='POST':
            product_ids=request.POST.getlist('id[]')
            for id in product_ids:
                productx = Product.objects.get(id=id)
                productx.modelnumber 
    return render(request, 'productmatchedit.html', {'bestbuyproduct': productx})

# ****************** Unmaches *******************

class deletematch(View):
    def get(self, request):
        allproduct=Deleteproductmatch.objects.all()
        context={
            'products':allproduct
        }
        return render(request, 'deletematch.html', context)


def matchunmach(request):
    if request.method=='POST':
            product_ids=request.POST.getlist('id[]')
            raw_num = random.randrange(0, 10000)
            for id in product_ids:
                product = Deleteproductmatch.objects.get(id=id)
                product.matchid = request.POST.get('raw_num', int(raw_num))
                product.save()
            return redirect('productview')

def unmatchunmatch(request):
    if request.method=='POST':
            product_ids=request.POST.getlist('id[]')
            for id in product_ids:
                product = Deleteproductmatch.objects.get(id=id)
                product.matchid = request.POST.get('raw_num')
                product.save()
            return redirect('productview')

def returnunmaches(request):
    if request.method=='POST':
            product_ids=request.POST.getlist('id[]')
            for id in product_ids:
                product = Deleteproductmatch.objects.get(id=id)
                product.delete()
            return redirect('productview')

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Product.objects.get(ProductsKey=producto_id)
    carrito.agregar(producto)
    return redirect("productview")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Product.objects.get(ProductsKey=producto_id)
    carrito.eliminar(producto)
    return redirect("productview")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Product.objects.get(ProductsKey=producto_id)
    carrito.restar(producto)
    return redirect("productview")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("productview")



# ****************** Vendors *******************

def bestbuy(request, *args, **kwargs):
    bestbuy = Bestbuymodel.objects.all()
    return render(request, 'bestbuy.html', {'bestbuyproduct': bestbuy})

def lowes(request):
    lowes = Lowesmodel.objects.all()
    return render(request, 'lowes.html', {'lowesproduct': lowes})

def homedepot(request):
    homedepot = Homemodel.objects.all()
    return render(request, 'homedepot.html', {'homedepotproduct': homedepot})

def walmart(request):
    walmart = Walmartmodel.objects.all()
    return render(request, 'walmart.html', {'walmartproduct': walmart})


# ****************** Product master *******************

def bestbuymaster(request):
    bestbuymaster = Bestbuymodel.objects.all()
    return render(request, 'bestbuymaster.html', {'bestbuyproductmaster': bestbuymaster})

def lowesmaster(request):
    lowesmaster = Lowesmodel.objects.all()[:100:1]
    return render(request, 'lowesmaster.html', {'lowesproductmaster': lowesmaster})

def homedepotmaster(request):
    homedepotmaster = Homemodel.objects.all()
    return render(request, 'homedepotmaster.html', {'homedepotproductmaster': homedepotmaster})


# ****************** Modals vendors *******************

def bestbuyview(request, prod_id):
    bestbuyview = Bestbuymodel.objects.get(upc=prod_id)
    return render(request, "bestbuyview.html", {'product': bestbuyview})

def lowesview(request, prod_id):
    #lowesview = Bestbuymodel.objects.get(OmniitemId.product.barcode=prod_id)  #Errors of sintax
    return render(request, "lowesview.html", {'product': lowesview})

def homedepotview(request, prod_id):
    homedepotview = Homemodel.objects.get(itemId=prod_id)
    return render(request, "homedepotview.html", {'product': homedepotview})

def walmartview(request, prod_id):
    walmartview = Walmartmodel.objects.get(upc=prod_id)
    return render(request, "walmartview.html", {'product': walmartview})


# ****************** Modals products master *******************

def bestbuymasterview(request, prod_id):
    bestbuymasterview = Bestbuymodel.objects.get(upc=prod_id)
    return render(request, "bestbuymasterview.html", {'product': bestbuymasterview})

def lowesview(request, prod_id):
    lowesview = Lowesmodel.objects.get(itemNumber=prod_id)
    return render(request, "lowesview.html", {'product': lowesview})

def homedepotmasterview(request, prod_id):
    homedepotmasterview = Homemodel.objects.get(itemId=prod_id)
    return render(request, "homedepotmasterview.html", {'product': homedepotmasterview})






def bestbuyjson(request):
    bestbuyjsons = Bestbuymodel.objects.all()
    data = [bestbuyjson.get_data() for bestbuyjson in bestbuyjsons]
    response = {'data': data}
    return JsonResponse(response)

def lowesjson(request):
    lowesjsons = Lowesmodel.objects.all()
    data = [lowesjson.get_data() for lowesjson in lowesjsons]
    response = {'data': data}
    return JsonResponse(response)

def add_product(request):
    if request.method == "POST":
        if request.POST.get('category') \
            and request.POST.get('matchid')  \
            and request.POST.get('modelnumber') \
            and request.POST.get('brand') \
            and request.POST.get('loweomniid') \
            and request.POST.get('lowesdescription') \
            and request.POST.get('homedepotitemid') \
            and request.POST.get('homedepotproductlabel') \
            and request.POST.get('bestbuysku') \
            and request.POST.get('bestbuyproductname') \
            and request.POST.get('matched') \
            or request.POST.get('delete'):
            product = Productlist()
            product.category = request.POST.get('category')
            product.matchid = request.POST.get('matchid')
            product.modelnumber = request.POST.get('modelnumber')
            product.brand = request.POST.get('brand')
            product.loweomniid = request.POST.get('loweomniid')
            product.lowesdescription = request.POST.get('lowesdescription')
            product.homedepotitemid = request.POST.get('homedepotitemid')
            product.homedepotproductlabel = request.POST.get('homedepotproductlabel')
            product.bestbuysku = request.POST.get('bestbuysku')
            product.bestbuyproductname = request.POST.get('bestbuyproductname')
            product.matched = request.POST.get('matched')
            product.delete = request.POST.get('delete')
            product.save()
            messages.success(request, "Add successfully!")
            return HttpResponseRedirect("/productlist")
    else:
            return render(request, 'add.html')



def productlist(request):
    productlist = Productlist.objects.all()
    return render(request, 'productlist.html', {'productlist': productlist})


def singledayrun(request):
    products7 = DevopsBestBuy.objects.all()
    @register.filter("mongo_id")
    def mongo_id(value):
        return str(value['_id'])
    return render(request, 'singledayrun.html', {'products7': products7})

def multidayrun(request):
    return render(request, "multidayrun.html")

def multidayrunjson(request):
    multidayrunjsons = DevopsBestBuy.objects.all()
    data = [multidayrunjson.get_data() for multidayrunjson in multidayrunjsons]
    response = {'data': data}
    return JsonResponse(response)


def about(request):
    return render(request, 'about.html')


def editviewbestbuy(request, prod_id):
    product = Bestbuymodel.objects.get(upc=prod_id)
    return render(request, "editviewbestbuy.html", {'product': product})
   

def editbestbuy(request):
    if request.method == 'POST':
        product = Bestbuymodel.objects.get(upc=request.POST.get('upc'))
        if product != None:
            product.name = request.POST.get('name')
            product.save()
            messages.success(request, "Product Updated successfully !")
            return HttpResponseRedirect("/")


def Login(request):
    if request.user == None or request.user == "" or request.user.username == "":
        return render(request, "login.html")
    else:
        return HttpResponseRedirect('/') 

def LoginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user != None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Enter your data correctly")
            return HttpResponseRedirect('/')

def LogoutUser(request):
    logout(request)
    request.user = None
    return HttpResponseRedirect('/')
