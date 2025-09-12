from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return render(request, "home.html")

def aboutus(request):
    return render(request, "aboutus.html")

def loginpage(request):
    return render(request, "auth/login.html")

def signuppage(request):
    return render(request, "auth/signup.html")