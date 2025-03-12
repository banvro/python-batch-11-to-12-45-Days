from django.shortcuts import render, redirect
from todo.models import mytodo

# Create your views here.

def homepage(request):
    data = mytodo.objects.all()
    return render(request, "todohome.html", {"alldata" : data})


def contact(request):
    return render(request, "contactus.html")

def saving(request):
    if request.method == "POST":
        t = request.POST.get("title")
        m = request.POST.get("desc")

        data = mytodo(title = t, discption = m)
        data.save()

        return redirect("/")


def deletethis(request, id):
    
    data = mytodo.objects.get(id = id)
    
    data.delete()

    return redirect("/")


def updating(request, myid):
    data = mytodo.objects.get(id = myid)

    return render(request, "updatetodo.html", {"data" : data})


def updatingnow(request, myid):
    data = mytodo.objects.get(id = myid)

    if request.method == "POST":
        t = request.POST.get("title")
        m = request.POST.get("desc")

        data.title = t
        data.discption = m 

        data.save()


    return redirect("/")