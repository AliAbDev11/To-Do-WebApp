from django.shortcuts import render, redirect, get_object_or_404
from .models import List, Task
from .forms import ListForm, TaskForm

def home(request):
    lists = List.objects.all()
    return render(request, 'home.html', {'lists': lists})

def create_list(request):
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ListForm()
    return render(request, 'list_crud/create_list.html', {'form': form})

def update_list(request, pk):
    list_instance = get_object_or_404(List, pk=pk)
    if request.method == 'POST':
        form = ListForm(request.POST, instance=list_instance)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ListForm(instance=list_instance)
    return render(request, 'list_crud/update_list.html', {'form': form})

def delete_list(request, pk):
    list_instance = get_object_or_404(List, pk=pk)
    if request.method == 'POST':
        list_instance.delete()
        return redirect('home')
    return render(request, 'list_crud/delete_list.html', {'list': list_instance})

def list_detail(request, pk):
    list_instance = get_object_or_404(List, pk=pk)
    return render(request, 'list_crud/list_detail.html', {'list': list_instance})