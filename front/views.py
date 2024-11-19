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

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('/')  # Replace 'home' with your desired redirect URL name
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')