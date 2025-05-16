from django.shortcuts import render
from django.http import HttpResponse

from articals.models import ContactUs
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

def saveinfo(request):
    if request.method == "POST":
        full_name = request.POST.get("fname")
        email = request.POST.get("email")
        phon = request.POST.get("pnum")
        measg = request.POST.get("msg")

        data = ContactUs(user_full_name = full_name, email = email, phone_number = phon, message = measg)

        data.save()

    return HttpResponse("data saved sucessfully.........!")