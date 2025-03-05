from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Contactinfo
# Create your views here.

def home(request):
    return render(request, "home.html")

def aboutus(request):
    return render(request, "aboutus.html")


def contactus(request):
    return render(request, "contactus.html")

def servicesus(request):
    return render(request, "services.html")



def savingdata(request):
    if request.method == "POST":
        full_name = request.POST.get("fname")
        email_addres = request.POST.get("email")
        p_number = request.POST.get("pnumbr")
        message = request.POST.get("msg")

        data = Contactinfo(full_name = full_name, email = email_addres, phone_number = p_number, message = message)

        data.save()


    return HttpResponse("data saved sucessfully...")


def allforms(request):

    data = Contactinfo.objects.all()

    return render(request, "allforms.html", {"alldta" : data})