from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact
from math import ceil
# Create your views here.
def index(request):
    # products= Product.objects.all()
    # n=len(products)
    # nSlides = n//4 + ceil(((n//4)-n)//4)
    # # parameter={'no_of_slides':nSlides,'range':range(1,nSlides),'product':products}
    # allProds=[[products, range(1,nSlides),nSlides],
    # [products, range(1,nSlides),nSlides]]
    allProds=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nSlides = n//4 + ceil(((n//4)-n)//4)
        allProds.append([prod,range(1,nSlides),nSlides])
    parameter={'allProds':allProds}
    return render(request,'shop/index.html',parameter)

def about(request):
    return render(request,'shop/about.html')

def Language(request):
    return render(request,)

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        message=request.POST.get('message','')        
        # print(name,email,phone,message)
        contact=Contact(name=name,email=email,phone=phone,message=message)
        contact.save()

    return render(request,'shop/contact.html')

def buyagain(request):
    return render(request,)


def tracker(request):
    return render(request,'shop/tracker.html')


def search(request):
    return render(request,'shop/search.html')


def productView(request,myid):
    #Fetch the product using id
    product=Product.objects.filter(id=myid)
    return render(request,'shop/prodView.html',{'product':product[0]})

def checkout(request):
    return render(request,'shop/checkout.html') 