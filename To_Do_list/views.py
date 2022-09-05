from django.shortcuts import render

# Create your views here.
from To_Do_list.additemform import AddItem
from To_Do_list.models import Products
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages

def additemview(request):
    dbname=None
    #message = None
    form=AddItem()

    #print("############",prod_disp.name())
    #return render(request,'To_Do_list/products.html',{'form':form,'namedb':namedb})
    submit=False

    if request.method == 'POST':
        name=request.POST['name']

        quantity=request.POST['quantity']
        request.session[name]=quantity
        request.session.set_expiry(180)
        for key in list(request.session.keys()):
            if key.startswith("_"):
                del request.session[key]
            submit=True

        #if request.session[name] != request.POST['name']:
    #    for key in list(request.session.keys()):
        #        if not key.startswith("_"): # skip keys set by the django system
        #            del request.session[key]


        #request.session.set_expiry(180)
        ###             del request.session[key]


        #return HttpResponseRedirect('/To_Do_list/products.html')

        #return render(request,'To_Do_list/products.html',{'form':form,'prod_disp':prod_disp})
    prod_disp=Products.objects.all()


    return render(request,'To_Do_list/products.html',{'form':form,'submit':submit,'prod_disp':prod_disp})





def displayitemview(request):
    #prod_disp=ProductsSel.objects.all()
    return render(request,'To_Do_list/displayitems.html')
