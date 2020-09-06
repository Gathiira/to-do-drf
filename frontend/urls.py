from django.urls import path

from .views import listTask

urlpatterns = [
    path('', listTask, name='list_task'),
]