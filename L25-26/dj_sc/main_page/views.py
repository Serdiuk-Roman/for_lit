from django.shortcuts import render
from django.http import HttpResponse
from .redis_for_view import run_task

from .models import PorterItem

# Create your views here.


from django.views.generic import TemplateView, ListView


class IndexView(TemplateView):
    template_name = "main_page/index.html"


class ResListView(ListView):
    model = PorterItem


def start_scrap(request):
    print("def start_scrap")
    run_task()
    return HttpResponse("You're looking at sile.")
