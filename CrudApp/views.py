from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from CrudApp.form import TaskForm

# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def task_detail(request,id):
    task = get_object_or_404(Task, id=id)
    return render(request, 'task_details.html', {'tasks': task})

# create
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})

def task_edit(request,id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        form = TaskForm(request.Post, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', id=task.id)
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form})

# delete
def task_delete(request,id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    else:
        task = TaskForm(instance=task)
    return render(request, 'task_confirm_delete.html', {'task': task})
