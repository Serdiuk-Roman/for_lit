# from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.


class BlogIndex(TemplateView):
    template_name = "post/index.html"
