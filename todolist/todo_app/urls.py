from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('tasklist/', views.tasklist, name='tasklist'),  # This is the POST action URL
    path('tasks/<int:id>/', views.task_detail, name='task_detail'),  # This is the task detail view

]