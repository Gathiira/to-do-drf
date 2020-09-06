from django.shortcuts import render

# Create your views here.

def listTask(request):
    return render(request, 'frontend/list-task.html',{})
