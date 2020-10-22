from django.http import HttpResponse
from django.shortcuts import render
from listproduct.models import listedproducts

def index(request):
    listprod = listedproducts.objects.all()[0:6]
    params = {'listprod':listprod}

    return render(request,'index.html',params)

def listproducts(request):
    return render(request,'productlisting.html') 