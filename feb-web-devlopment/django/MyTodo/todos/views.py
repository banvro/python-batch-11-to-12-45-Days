from django.shortcuts import render, redirect
from todos.models import mytodo
# Create your views here.

def homepage(request):
    alltodos = mytodo.objects.all().order_by("-id")
    return render(request, "homepage.html", {"alltodo" : alltodos})

def myalltodos(request):
    return render(request, "alltodos.html")


def savethinthistodo(request):
    if request.method == "POST":
        title = request.POST.get("title")
        desctitpn = request.POST.get("desc")

        savethis = mytodo(title = title, discription = desctitpn)
        savethis.save()

    return redirect("home")


def donetodo(request, id):
    todo = mytodo.objects.get(id = id)

    todo.tododone = True
    todo.save()

    return redirect("home")

def deletetodo(request, id):
    todo = mytodo.objects.get(id = id)

    todo.delete()

    return redirect("home")
