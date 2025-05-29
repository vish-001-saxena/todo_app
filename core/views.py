from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # redirect to named URL pattern 'home'
    else:
        form = TaskForm()

    tasks = Task.objects.all()
    return render(request, 'core/index.html', {'form': form, 'tasks': tasks})  # template path fixed

def task_list(request):
    tasks = Task.objects.all().order_by('scheduled_date')
    form = TaskForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('task_list')
    return render(request, 'todo/task_list.html', {'form': form, 'tasks': tasks})

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    return redirect('home')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    form = TaskForm(request.POST or None, instance=task)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('task_list')
    return render(request, 'core/edit_task.html', {'form': form})  # template path fixed
