from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return HttpResponse("This is my home page...")

def aboutus(request):
    return HttpResponse("This is about us page")

def contactus(request):
    return HttpResponse("<h1>This is Contact us page..</h1>")