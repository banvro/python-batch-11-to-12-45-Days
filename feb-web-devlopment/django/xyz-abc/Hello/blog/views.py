from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from blog.models import ContactUs

def home(request):
    return render(request, "home.html")

def aboutus(request):
    return render(request, "about.html")


def contactus(request):
    return render(request, "contactus.html")


def servicesus(request):
    # ORM 
    my_data = ContactUs.objects.all().order_by("-id")

    context = {"records" : my_data}
    return render(request, "services.html", context)



def savethisdaa(request):
    if request.method == "POST":
        fullname = request.POST.get("fname")
        # fullname = request.POST["fname"]
        
        email = request.POST.get("email")
        phonenumer = request.POST.get("number")
        message = request.POST.get("msg")

        mydata = ContactUs(username = fullname, useremail = email, phone_number = phonenumer, message = message)
        mydata.save()

        return redirect("contact")

    # return HttpResponse(f"data saved sucessfully.....! {fullname}, {email} {phonenumer}, {message}")