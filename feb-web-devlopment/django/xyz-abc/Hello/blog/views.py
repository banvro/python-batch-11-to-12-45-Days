from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from blog.models import ContactUs
from django.core.mail import EmailMessage
from django.contrib import messages
from django.contrib.auth.models import User

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
        myimg = request.FILES.get('img')

        myemailmessage = f""""
        this is user contact us form data
        
        User Name :  {fullname}
        User Email :   {email}
        Phone Number:  {phonenumer}
        Message :     {message}
        
        THANK YOU :)
        """

        # mail = EmailMessage("This Email Comming from Django", myemailmessage, "banvro07@gmail.com", ["banvro07@gmail.com", "anchalrahi0@gmail.com", "sweetpreet.kaur1@gmail.com"])

        # mail.send()

        mydata = ContactUs(username = fullname, useremail = email, phone_number = phonenumer, message = message, myimage = myimg)
        mydata.save()

        messages.success(request, "Your Data Saved Sucessfully in database")
        # messages.info(request, "Your Data Saved Sucessfully in database")
        # messages.warning(request, "Your Data Saved Sucessfully in database")
        # messages.error(request, "Your Data Saved Sucessfully in database")



        return redirect("services")
    

    # return HttpResponse(f"data saved sucessfully.....! {fullname}, {email} {phonenumer}, {message}")




def deletethisdata(request, myid):
    
    # data = ContactUs.objects.all()
    data = ContactUs.objects.get(id = myid)
    data.delete()

    messages.warning(request, "Your Data Deleteed From database...! :)")

    return redirect("services")



def updatethisdata(request, xyz):
    
    data = ContactUs.objects.get(id = xyz)

    return render(request, "contactus-update.html", {"yourdata" : data})


def updatedatanow(request, upateid):
    if request.method == "POST":
        fullname = request.POST.get("fname")
        # fullname = request.POST["fname"]
        
        email = request.POST.get("email")
        phonenumer = request.POST.get("number")
        message = request.POST.get("msg")

        mydata = ContactUs.objects.get(id = upateid)

        mydata.username = fullname
        mydata.useremail = email
        mydata.phone_number = phonenumer
        mydata.message = message

        mydata.save()


    return redirect("services")



# email 
# django forms 
# Session 
# cookies 
# Authantication system 


def searchthisdata(request):
    xyz = request.GET['query']

    searchdata = ContactUs.objects.filter(username = xyz) or ContactUs.objects.filter(phone_number = xyz)

    context = {"records" : searchdata}

    return render(request, "services.html", context)



def signup(request):
    if request.method == "POST":
        usernae = request.POST.get("Username")
        email = request.POST.get("email")
        Password = request.POST.get("Password")
        FullName = request.POST.get("FullName")

        saveuser = User.objects.create_user(username = usernae, email = email, password=Password, first_name = FullName)
        saveuser.save()

        messages.success(request, "User Added Sucessfulyy.....!")



    return render(request, "signup.html")