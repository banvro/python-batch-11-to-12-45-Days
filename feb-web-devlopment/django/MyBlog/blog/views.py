from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hommepage(request):
    return HttpResponse("this is my first home page.....")

def aboutus(request):
    return HttpResponse("this is about us apge")