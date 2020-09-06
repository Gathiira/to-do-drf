from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Task
from .serializers import TaskSerializer

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'list':'/task-list/',
        'Detail View': '/task-create/',
        'Create': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }
    return JsonResponse('API BASE POINT', safe=False)

class TaskListApiView(APIView):
    def get(self, request):
        tasks = Task.objects.all().order_by('id')
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTPP_400_BAD_REQUEST)

class TaskDetailApiView(APIView):
    def get_object(self, id):
        try:
            return Task.objects.get(pk=id)
        except Task.DoesNotExist:
            return Response(status=status.HTPP_404_NOT_FOUND)
    
    def get(self, request, id):
        task = self.get_object(id)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, id):
        serializer = TaskSerializer(self.get_object(id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTPP_400_BAD_REQUEST)

    def delete(self, request, id):
        task = self.get_object(id)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
