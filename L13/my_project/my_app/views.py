from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Task

# Create your views here.


def index(request):
    tasks = Task.objects.all()

    return render(
        request,
        'my_app/index.html',
        {'tasks': tasks}
    )


def create_task(request):
    if request.method == 'POST':
        task = Task(
            text=request.POST.get('text'),
            checked=bool(request.POST.get('checked', False))
        )
        task.save()
    return redirect('/tasks')


def task_detail(request, pk):
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        print("except")
    return render(
        request,
        'my_app/detail.html',
        {'task': task}
    )
