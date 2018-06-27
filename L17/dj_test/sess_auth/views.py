# Create your views here.
from django.views.generic.edit import CreateView
from .forms import AuthModelForm
from .models import Task
from django.http import HttpResponse


class AuthFormView(CreateView):
    form_class = AuthModelForm
    template_name = 'sess_auth/login.html'


def taskView(request):
    task = Task.objects.all()
    return HttpResponse(task)
