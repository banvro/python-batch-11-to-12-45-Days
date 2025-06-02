from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist.models import addtodo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect("login")

def task(request):
    if request.user.is_authenticated:
        data = addtodo.objects.all().order_by("-id")
        return render(request, "task.html", {"allData" : data})
    else:
        return redirect("/login")

def saveinfo(request):

    if request.method == "POST":
        task_s = request.POST.get("tsk")
        descptn = request.POST.get("desp")

        data = addtodo(ta_sk=task_s, descri_ption=descptn)
        data.save()
        return redirect("task")
    return HttpResponse("Tasks added successfully...","task")
    
def deletetask(request, xyz):
    data = addtodo.objects.get(id = xyz)
    data.delete()
    return redirect("task") 

def updatetask(request, myid):
    data = addtodo.objects.get(id = myid)
    return render(request, "updatingdata.html", {"allData" : data})

def updating(request,myid):

    if request.method == "POST":
        task_s = request.POST.get("tsk")
        descptn = request.POST.get("desp")

        data = addtodo.objects.get(id = myid)

        data.ta_sk = task_s
        data.descri_ption = descptn
        
        data.save()
        return redirect("task")




def loginpage(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        password = request.POST.get("password")

        print(username, password, "ooooooooooooo")

        usercheck = authenticate(username = username, password = password)
        print(usercheck, "eeeeeeeeeeeeeeee")

        if usercheck is not None:
            login(request, usercheck)

            return redirect("/")
        else:
            return redirect("/login")


    return render(request, "auth/login.html")

def registerpage(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        fulnam = request.POST.get("fname")
        email = request.POST.get("email")
        password = request.POST.get("password")

        User.objects.create_user(username = username, first_name = fulnam, email = email, password = password)


    return render(request, "auth/signup.html")


def logoutuser(request):
    logout(request)

    return redirect("/login")