from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User,Product
# Create your views here.
def myapp(request):
    myusers=User.objects.all().values()
    myproducts=Product.objects.all().values()
    template = loader.get_template('index.html')
    context={
        'userlist':myusers,
        'productlist':myproducts
    }
    return HttpResponse(template.render(context,request))

def userlogin(request):
    #return Httpresponse("this login page is yet to built..")
    template2=loader.get_template('login.html')
    return HttpResponse(template2.render(
    ))

def prod_details(request,id): #handling the http request depending on the id value recived from url pattern requested
    product=Product.objects.get(id=id) #select * from Product where id = <some_id_number>
    context={
        'product' : product
    }
    template = loader.get_template('prod_details.html')   
    return HttpResponse(template.render(context, request))