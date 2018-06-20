from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.views.generic import TemplateView

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView

from .models import Task
from .forms import TaskModelForm, TaskForm


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


class IndexView(TemplateView):

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


class TaskListView(ListView):
    model = Task

    def get_context_data(self):
        context = super().get_context_data()
        context['form'] = TaskModelForm()
        return context


class TaskDetailView(DetailView):
    model = Task


class TaskFormView(FormView):
    template_name = 'my_app/contact.html'
    form_class = TaskForm
