from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    # return HttpResponse("<h1>This is home page..</h1>")

    username = "rat"

    table = [f"2 x {i} = {2*i}" for i in range(1, 11)]

    # print(table)

    alldata = {"data" : username, "mytable" : table}

    return render(request, "home.html", alldata)

def aboutus(request):
    # return HttpResponse("<h1>This is aboutus page..</h1>")
    table = [f"2 x {i} = {2*i}" for i in range(1, 11)]
    return render(request, "aboutus.html", {"mytable" : table})

def contactus(request):
    # return HttpResponse("<h1>This is contactus page..</h1>")
    return render(request, "contact.html")

