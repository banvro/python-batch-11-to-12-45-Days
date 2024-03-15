from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from xyzapi.serializer import TodoSerializer
from xyzapi.models import MyTodo

# Create your views here.

@api_view(['GET'])
def alltods(request):
    alltodo = MyTodo.objects.all().order_by("-id")
    mydata = TodoSerializer(alltodo, many = True)

    return Response({
        "message" : "Data Fetch Sucessfully",
        "data" : mydata.data
    })



@api_view(['POST'])
def savethistodo(request):
    serlizedata = TodoSerializer(data = request.data)
    if serlizedata.is_valid():
        serlizedata.save()

    return Response({
        "message" : "Data saved Sucessfully",
        "data" : serlizedata.data
    })


@api_view(['GET'])
def singlethistodo(request, id):
    alltodo = MyTodo.objects.get(id = id)
    mydata = TodoSerializer(alltodo)

    return Response({
        "message" : "todo feethc Sucessfully",
        "data" : mydata.data
    })