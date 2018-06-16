from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.views.generic import TemplateView as View

from .models import Task
from .forms import TaskModelForm

# Create your views here.


# def index(request):
#     tasks = Task.objects.all()

#     return render(
#         request,
#         'my_app/index.html',
#         {'tasks': tasks, 'form': TaskModelForm()}
#     )


# def create_task(request):
#     if request.method == 'POST':
#         form = TaskModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/tasks')
#         tasks = Task.objects.all()
#         return render(
#             request,
#             'my_app/index.html',
#             {'tasks': tasks, 'form': form}
#         )
#     return redirect('/tasks')


def task_detail(request, pk):
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        print("except")

    if request.method == 'POST':
        form = TaskModelForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/tasks/{}'.format(task.pk))
    else:
        form = TaskModelForm(instance=task)

    return render(
        request,
        'my_app/detail.html',
        {'task': task, 'form': form}
    )


class IndexView(View):

    def get(self, request, *args, **kwarg):
        tasks = Task.objects.all()
        return render(
            request,
            'my_app/index.html',
            {'tasks': tasks, 'form': TaskModelForm()}
        )

    def post(self, request, pk=None):
        if request.method == 'POST':
            form = TaskModelForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/tasks')
            tasks = Task.objects.all()
            return render(
                request,
                'my_app/index.html',
                {'tasks': tasks, 'form': form}
            )
        return redirect('/tasks')
