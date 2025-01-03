from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import TaskListForm, TaskForm
from django.http import HttpResponse
from django.urls import reverse
from .models import *

# Create your views here.
def index(request):
    # Check if the user is authenticated
    if not request.user.is_authenticated:
        # If the user is not authenticated, redirect them to the login page
        return redirect('login')  # Make sure 'login' matches the name of your login URL pattern

    context = {
        'Taskslist': TaskList.objects.filter(user=request.user),  # Filter by logged-in user
    }
    return render(request, 'pages/index.html', context)

# View to handle adding a new task list
@login_required
def tasklist(request):
    if request.method == "POST":
        add_Tasklist = TaskListForm(request.POST)
        if add_Tasklist.is_valid():
            # Associate the task list with the current user
            add_Tasklist.instance.user = request.user
            add_Tasklist.save()
            return redirect('tasklist')  # Redirect to the task list view after saving
    else:
        add_Tasklist = TaskListForm()

    # Fetch all existing task lists to display in the sidebar
    context = {
        'TaskListForm': add_Tasklist,
        'Taskslist': TaskList.objects.filter(user=request.user),
    }
    return render(request, 'pages/index.html', context)


# View to handle displaying the details of a specific task list
@login_required
def task_detail(request, id):
    # Fetch the task list by its ID or return a 404 if not found
    tasklist = get_object_or_404(TaskList, id=id)
    tasks = Task.objects.filter(tasklist=tasklist)  # All tasks in this task list
    completed_tasks = tasks.filter(completed=True)  # Only completed tasks

    if request.method == "POST":
        print("POST request received")
        print(f"POST data: {request.POST}")

        add_task = TaskForm(request.POST)
        if add_task.is_valid():
            task = add_task.save(commit=False)  # Don't save to the DB yet
            task.tasklist = tasklist  # Associate the task with the current tasklist
            task.user = request.user  # Associate the task with the current user
            task.save()  # Now save the task
            print("Task saved successfully")
            return redirect('task_detail', id=tasklist.id)  # Redirect back to the task detail page
        else:
            print("Form is invalid")
            print(add_task.errors)  # Print any form validation errors
    else:
        print("GET request received")
        add_task = TaskForm()

    # Pass the selected task list to the template cc
    context = {
        'completed_tasks': completed_tasks,
        'tasksform': add_task,
        'tasklist': tasklist,
        'Taskslist': TaskList.objects.filter(user=request.user),
        'Tasks': Task.objects.filter(tasklist=tasklist),  # Show only tasks related to this task list
    }
    return render(request, 'pages/task_detail.html', context)

# View to handle task status
def toggle_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed  # Toggle the completed status
    task.save()
    return redirect('task_detail', task.tasklist.id)  # Redirect back to the task list

# Update task view
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.title = request.POST.get("title")
        task.description = request.POST.get("description", "")
        task.save()
        return redirect('task_detail', task.tasklist.id)

# Delete task view
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    tasklist_id = task.tasklist.id  # Get the task list id before deleting
    task.delete()
    return redirect('task_detail', tasklist_id)

# Update task list view
def update_tasklist(request, tasklist_id):
    tasklist = get_object_or_404(TaskList, id=tasklist_id)
    if request.method == 'POST':
        new_title = request.POST.get('title')
        tasklist.title = new_title
        tasklist.save()
        return redirect('index')  # Redirect to home or any page that lists the task lists

# Delete task list view
def delete_tasklist(request, tasklist_id):
    tasklist = TaskList.objects.get(id=tasklist_id)
    if request.method == 'POST':
        tasklist.delete()
        return redirect('tasklist') 