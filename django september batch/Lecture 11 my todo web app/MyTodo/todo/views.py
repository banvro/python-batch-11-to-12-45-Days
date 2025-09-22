from django.shortcuts import render, redirect
from todo.models import myTodo
from django.contrib import messages

# Create your views here.

def todohome(request):
    all_todos = myTodo.objects.all()
    return render(request, "todowork.html", {"todos" : all_todos})

def savingtodo(request):
    if request.method == "POST":
        titl = request.POST.get("title")
        desc = request.POST.get("msg")

        data = myTodo(title = titl, dexription = desc)
        data.save()

        messages.success(request, "Todo Added Sucessfully...")

        return redirect("todo")

def deletetodo(request, x):
    todo = myTodo.objects.get(id = x)
    todo.delete()

    messages.warning(request, "Todo Deletd sucessfully...!")

    return redirect("todo")


def todoupdate(request, xyz):
    todo = myTodo.objects.get(id = xyz)
    if request.method == "POST":
        titl = request.POST.get("title")
        desc = request.POST.get("msg")

        todo.title = titl
        todo.dexription = desc
        todo.save()

        messages.info(request, "todo updated sucessfully....!")
    return redirect("todo")