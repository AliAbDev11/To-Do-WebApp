from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('tasklist/', views.tasklist, name='tasklist'),  # This is the POST action URL
    path('tasks/<int:id>/', views.task_detail, name='task_detail'),  # This is the task detail view
    path('toggle-task-status/<int:task_id>/', views.toggle_task_status, name='toggle_task_status'),
    path('delete-task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('update-task/<int:task_id>/', views.update_task, name='update_task'),
]