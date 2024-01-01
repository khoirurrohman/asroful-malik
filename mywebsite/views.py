from django.shortcuts import render

def index(request):
    return render(request,'index.html',)

def product(request):
    return render(request,'product.html',)

def contact(request):
    return render(request,'contact.html',)

def menu(request):
    return render(request,'menu.html',)



# Create your views here.
