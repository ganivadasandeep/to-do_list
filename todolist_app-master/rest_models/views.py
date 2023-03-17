from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
from rest_framework import status
@api_view(['GET'])
def indexofrest(request):
    return Response('Working')

@api_view(['GET','POST'])
def alltasks(request):
    if request.method == "GET":
        tasks = Task.objects.all()
        serialized = TaskSerializer(tasks,many=True)
        return Response(serialized.data)
    if request.method == "POST":
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST','DELETE'])
def taskX(request,pk):
    if request.method == "GET":
        tasks = Task.objects.get(id=pk)
        serialized = TaskSerializer(tasks,many=False)
        return Response(serialized.data)
    if request.method == "POST":
        tasks = Task.objects.get(id=pk)        
        serializer = TaskSerializer(instance=tasks,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        tasks = Task.objects.get(id=pk)     
        tasks.delete()
        return Response('Successfully deleted.')
