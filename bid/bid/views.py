from django.http import HttpResponse
from django.shortcuts import render
from listproduct.models import listedproducts

def index(request):
    listprod = listedproducts.objects.all()[0:6]
    loggedin = request.GET.get('loggedin',False)
    username = request.GET.get('username','nothing')
    
    if loggedin == False:
        params = {'dontshowpage':True}
        return render(request,'index.html',params)
    else:
        params = {'listprod':listprod,'username':username}
        return render(request,'index.html',params)
