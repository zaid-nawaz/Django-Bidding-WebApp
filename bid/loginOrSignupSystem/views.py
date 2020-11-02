# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from loginOrSignupSystem.models import User

def login(request):
    if request.method == 'POST':
        Loginname = request.POST.get('Loginname','nothing')
        Loginpassword = request.POST.get('Loginpassword','nothing')
        seeifuserisreal = User.objects.filter(username=Loginname,userpassword=Loginpassword)
        if len(seeifuserisreal) == 1:
            params = {'succs':True,'showpage':True,'username':Loginname}
            
            return render(request,'login.html',params)
        elif len(seeifuserisreal) > 1 or len(seeifuserisreal) < 1:
            params = {'fails':True}
            return render(request,'login.html',params)
    # request.session['zaid'] = 'hello'
    # a = request.session['zaid']
    # print(a)
    return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('name','nothing')
        userphonenumber = request.POST.get('phonenumber',   'nothing')
        useraddress = request.POST.get('address',   'nothing')
        userpassword = request.POST.get('password', 'nothing')
        alreadyexistusername = User.objects.filter(username=username)
        alreadyexistuserpassword = User.objects.filter(userpassword=userpassword)
        if len(alreadyexistusername) > 0:
            params = {'alreadyexistusername':True,'fails':True}
            print(alreadyexistuserpassword)
        elif len(alreadyexistuserpassword) > 0:
            if userpassword == alreadyexistuserpassword[0].userpassword:
                params = {'alreadyexistuserpassword':True,'fails':True}
            
        else:
            dataofuser = User(username=username,userphonenumber=userphonenumber,useraddress=useraddress,userpassword=userpassword)
            dataofuser.save()
            params = {'success':True}
        return render(request,'signup.html',params)
    return render(request,'signup.html')
