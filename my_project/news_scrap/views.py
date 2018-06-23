# from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from news_scrap.models import ShortNews
from .forms import NewsModelForm, NewsForm


class NewsListView(ListView):
    model = ShortNews

    def get_context_data(self):
        context = super().get_context_data()
        context['form'] = NewsModelForm()
        return context


class NewsDetailView(DetailView):
    model = ShortNews


class NewsFormView(CreateView):
    # template_name = 'my_app/contact.html'
    model = ShortNews
    form_class = NewsForm
