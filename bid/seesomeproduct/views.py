# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from listproduct.models import listedproducts

# Create your views here.
def seesomeproduct(request):
    return render(request,'seesomeproduct.html')

def searchresult(query,item):
    if query.lower() in item.productname or query.lower() in item.productdesc.lower() or query.lower() in item.productcategory.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('searchbar','nothing')
    prod = listedproducts.objects.all()
    listofsearchitem = []
    i = 0
    for item in prod:
        if searchresult(query , prod[i]):
            listofsearchitem.append(item)
        i += 1
    params = {'listsearch':listofsearchitem}
    if len(listofsearchitem) == 0:
        params = {'sorry':True}
    return render(request,'seesomeproduct.html',params)