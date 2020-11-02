# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from listproduct.models import listedproducts
from seesomeproduct.models import Biddingprice
from datetime import datetime

# Create your views here.
def seesomeproduct(request):
    username = request.GET.get('username','nothing')
    request.session['username'] = username
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

def prodview(request):
    prodid = request.GET.get('productid','nothing')
    username = request.session['username']
    
    biddingmoney = request.POST.get('biddingmoney',0)
    prod = listedproducts.objects.filter(productid=prodid)
    high = Biddingprice.objects.filter(Bid_on_productid=prodid)
    if str(prod[0].biddingtimeperiod) == datetime.today().strftime('%Y-%m-%d'):
        def biddingdateisover():
            return True
    else:
        def biddingdateisover():
            return False
    arr =[]
    if len(high) > 0:
        for item in high:
            temp = item.biddingprice
            arr.append(temp)
        winner = Biddingprice.objects.filter(biddingprice=max(arr))
        winnername = winner[0].bidder
        
        paramss = {'prod':prod[0],'highestbid':max(arr),'biddingdateisover':biddingdateisover(),'winnername':winnername}
    else:
        paramss = {'prod':prod[0],'nothing':True,'biddingdateisover':biddingdateisover()}
    
    
    if request.method == 'POST':
        bidobj = Biddingprice.objects.filter(bidder=username,Bid_on_productid=prodid)
        if len(bidobj) > 0:
            bidobj.update(biddingprice=biddingmoney)
            params = {'prod':prod[0],'success':True,'highestbid':max(arr),'biddingdateisover':biddingdateisover()}
            return render(request,'abouttheproductpage.html',params)
        else:
            dataofbidding = Biddingprice(bidder=username,Bid_on_productid=prodid,biddingprice=biddingmoney)
            dataofbidding.save()
            arr.append(biddingmoney)
            params = {'prod':prod[0],'success':True,'highestbid':max(arr),'biddingdateisover':biddingdateisover()}
            return render(request,'abouttheproductpage.html',params)
    return render(request,'abouttheproductpage.html',paramss)