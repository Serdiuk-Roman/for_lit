#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.conf.urls import url
from news_scrap.views import NewsListView, NewsDetailView, \
    NewsFormView, NewsCreateView, NewsUpdateView, NewsDeleteView

urlpatterns = [
    url(
        r'(?P<pk>[0-9a-f\-]+)$',
        NewsDetailView.as_view(),
        name="news_detail"
    ),
    url(
        r'add/$',
        NewsFormView.as_view(),
        name="news_form"
    ),
    url(
        r'create/$',
        NewsCreateView.as_view(),
        name="news_create"
    ),
    url(
        r'(?P<pk>[0-9a-f\-]+)/udate/$',
        NewsUpdateView.as_view(),
        name="news_update"
    ),
    url(
        r'(?P<pk>[0-9a-f\-]+)/delete/$',
        NewsDeleteView.as_view(),
        name="news_delete"
    ),
    url(
        r'$',
        NewsListView.as_view(),
        name="news_list"
    ),
]
