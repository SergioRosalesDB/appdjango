from django.http import HttpResponse
from django.shortcuts import render
from itertools import product
from pyexpat.errors import messages
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from mi_app_2.models import Productlist

def productlist(request):
    productlist = Productlist.objects.all()
    return render(request, 'productlist.html', {'productlist': productlist})
