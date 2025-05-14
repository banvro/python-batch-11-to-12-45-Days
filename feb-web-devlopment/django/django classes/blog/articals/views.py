from django.shortcuts import render
from django.http import HttpResponse
# from django.http import HttpResponse
# Create your views here.

def homepage(request):
    # return HttpResponse("this is our home page....")
    return render(request, "home.html")

def aboutus(request):
    return render(request, "about.html")

def contactus(request):
    return render(request, "contact.html")

def servicesus(request):
    return render(request, "services.html")