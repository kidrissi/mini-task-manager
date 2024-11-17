from django.shortcuts import render

from task.models import Task

def index(request):
    tasks = Task.objects.all()
    context = {
    'message': 'Welcome to the Task Manager!',  # Example variable
    'tasks': tasks,    # Example list of tasks
    }
    return render(request, 'index.html', context)