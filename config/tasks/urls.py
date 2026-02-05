from django.urls import path
from .views import tasks_list_create, task_detail

urlpatterns = [
    path('', tasks_list_create, name='tasks_list_create'),
    path('<int:pk>/', task_detail, name='task_detail'),
]
