from django.shortcuts import render

# Create your views here.
 
def homee(request):
    return render(request, "homepage.html")

def aboutus(request):
    return render(request, "aboutus.html")

def contactus(request):
    return render(request, "contactus.html")

def services(request):
    return render(request, "services.html")

def loginn(request):
    return render(request, "auth/loginpage.html")

def signuppage(request):
    return render(request, "auth/signup.html")