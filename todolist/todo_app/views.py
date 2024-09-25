from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskListForm, TaskForm
from .models import *

# Create your views here.
def index(request):
    context = {
        'Taskslist': TaskList.objects.all(),
    }
    return render(request,'base.html', context)

# View to handle adding a new task list
def tasklist(request):
    if request.method == "POST":
        add_Tasklist = TaskListForm(request.POST)
        if add_Tasklist.is_valid():
            add_Tasklist.save()
            return redirect('tasklist')  # Redirect to the task list view after saving
    else:
        add_Tasklist = TaskListForm()

    # Fetch all existing task lists to display in the sidebar
    context = {
        'TaskListForm': add_Tasklist,
        'Taskslist': TaskList.objects.all(),
    }
    return render(request, 'base.html', context)


# View to handle displaying the details of a specific task list
def task_detail(request, id):
    # Fetch the task list by its ID or return a 404 if not found
    tasklist = get_object_or_404(TaskList, id=id)

    if request.method == "POST":
        add_task = TaskForm(request.POST)
        if add_task.is_valid():
            new_task = add_task.save(commit=False)  # Do not save to DB yet
            new_task.tasklist = tasklist  # Associate the task with the tasklist
            new_task.save()  # Now save it
            return redirect('task_detail', id=tasklist.id)  # Redirect to the same task list

    else:
        add_task = TaskForm()

    # Pass the selected task list to the template
    tasks = Task.objects.filter(tasklist=tasklist)  # Fetch tasks for this tasklist
    context = {
        'tasksform': add_task,
        'tasklist': tasklist,
        'Taskslist': TaskList.objects.all(),
        'Tasks': tasks,  # Only tasks related to this tasklist
    }
    return render(request, 'pages/task_detail.html', context)