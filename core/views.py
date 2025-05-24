from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()

    tasks = Task.objects.all()
    return render(request, 'core/index.html', {'form': form, 'tasks': tasks})
