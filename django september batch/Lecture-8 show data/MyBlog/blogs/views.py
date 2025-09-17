from django.shortcuts import render, redirect
from django.http import HttpResponse
from blogs.models import ContactUs, Employee

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

def savinginfo(request):
    if request.method == "POST":
        fullname = request.POST.get("fname")
        phonenumber = request.POST.get("pnumber")
        email = request.POST.get("email")
        measg = request.POST.get("msg")

        data = ContactUs(full_name = fullname, phone_number = phonenumber, email_address = email, message = measg)
        data.save()

        return redirect("contact")

    return HttpResponse("Data Saved Successfly....!")


def adding_employee(request):
    if request.method == "POST":
        name = request.POST.get("enum")
        branch = request.POST.get("branch")
        number = request.POST.get("epnum")

        data = Employee(e_name = name, e_branch = branch, e_p_num = number)
        data.save()
    
    return render(request, "add_employee.html")


def allcontactus(request):
    all_data = ContactUs.objects.all().order_by("-id")
    return render(request, "allcontactus_records.html", {"all_data" : all_data})


def allemployee(request):
    all_records = Employee.objects.all()
    return render(request, "all_employee.html", {"records" : all_records})