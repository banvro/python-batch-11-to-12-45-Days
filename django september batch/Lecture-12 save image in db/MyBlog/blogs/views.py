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
        contact_img = request.FILES.get("img")

        data = ContactUs(full_name = fullname, phone_number = phonenumber, email_address = email, message = measg, img = contact_img)
        data.save()

        return redirect("contact")

    return HttpResponse("Data Saved Successfly....!")


def adding_employee(request):
    if request.method == "POST":
        name = request.POST.get("enum")
        branch = request.POST.get("branch")
        number = request.POST.get("epnum")
        img = request.FILES.get("eimg")

        data = Employee(e_name = name, e_branch = branch, e_p_num = number, e_img = img)
        data.save()
    
    return render(request, "add_employee.html")


def allcontactus(request):
    all_data = ContactUs.objects.all().order_by("-id")
    return render(request, "allcontactus_records.html", {"all_data" : all_data})


def allemployee(request):
    all_records = Employee.objects.all()
    return render(request, "all_employee.html", {"records" : all_records})


def deletingemp(request, x):
    
    record = Employee.objects.get(id = x)
    record.delete()

    return redirect("allemp")

def contactdelete(request, xyz):
    recordd = ContactUs.objects.get(id = xyz)
    recordd.delete()

    return redirect("allforms")

def updateemp(request, update_id):
    record = Employee.objects.get(id = update_id)
    return render(request, "updateempdata.html", {"record" : record})

def empupdate(request, update_id):
    record = Employee.objects.get(id = update_id)

    if request.method == "POST":
        emp_name = request.POST.get("enum")
        branch = request.POST.get("branch")
        number = request.POST.get("epnum")

        record.e_name = emp_name
        record.e_branch = branch
        record.e_p_num = number
        record.save()

    return redirect("allemp")


def updatecontactform(request, contact_id):
    recrd = ContactUs.objects.get(id = contact_id)

    if request.method == "POST":
        fullname = request.POST.get("fname")
        phonenumber = request.POST.get("pnumber")
        email = request.POST.get("email")
        measg = request.POST.get("msg")

        recrd.full_name = fullname
        recrd.phone_number = phonenumber
        recrd.email_address = email
        recrd.message = measg
        recrd.save()

        return redirect("allforms")
