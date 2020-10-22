# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import listedproducts
# Create your views here.
def listproducts(request):
    if request.method =='POST':
        productimage = request.POST.get('productselector','')
        productname = request.POST.get('productname','')
        productdesc = request.POST.get('productdesc','')
        productprice = request.POST.get('price','')
        producttimeperiod = request.POST.get('holdingtimeperiod','')
        biddingtimeperiod = request.POST.get('biddingtimeperiod','')
        category = request.POST.get('category','')
        listprod = listedproducts(productname=productname,productImage=productimage,productdesc=productdesc,productprice=productprice,holdingtimeperiod=producttimeperiod,biddingtimeperiod=biddingtimeperiod,productcategory=category)
        listprod.save()
        
        return render(request,'productlisting.html') 
    return render(request,'productlisting.html') 