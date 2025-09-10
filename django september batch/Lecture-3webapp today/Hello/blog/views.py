from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def bloging1(reqiest):
    return HttpResponse("This is my first blog")

def bloging2(request):
    return HttpResponse("this is blog 2")