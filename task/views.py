from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from task.models import Task

def index(request):
    if request.user.is_authenticated:
        if  request.user.username=='khalid':
            tasks = Task.objects.all()
        else:
            tasks = Task.objects.filter(assigned_to=request.user)
    else:
        return render(request, 'login.html')
    context = {
    'message': 'Welcome to the Task Manager!',  # Example variable
    'tasks': tasks,    # Example list of tasks
    }
    return render(request, 'index.html', context)