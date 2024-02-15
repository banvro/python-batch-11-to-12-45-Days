from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home.html")

def aboutus(request):
    return render(request, "about.html")


def contactus(request):
    return render(request, "contactus.html")


def servicesus(request):
    return render(request, "services.html")

