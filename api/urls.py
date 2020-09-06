from django.urls import path

from .views import apiOverview, TaskListApiView, TaskDetailApiView

urlpatterns = [
    path('api/', apiOverview, name='api-overview'),
    path('task-list/', TaskListApiView.as_view(), name='task-list'),
    path('task-list/<int:id>/', TaskDetailApiView.as_view(), name='task-detail'),
]