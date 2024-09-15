from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list/create/', views.create_list, name='create_list'),
    path('list/<int:pk>/update/', views.update_list, name='update_list'),
    path('list/<int:pk>/delete/', views.delete_list, name='delete_list'),
    path('list/<int:pk>/', views.list_detail, name='list_detail'),
    # path('task/edit/<int:pk>/', views.edit_task, name='edit_task'),
    # path('task/delete/<int:pk>/', views.delete_task, name='delete_task'),
    # path('task/mark_complete/<int:pk>/', views.mark_task_complete, name='mark_task_complete'),
]