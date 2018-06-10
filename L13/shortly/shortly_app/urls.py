#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('new_url/', views.new_url),
    path('follow/<int:url_id>', views.follow_link),
    path('detail/<int:url_id>', views.link_detail),
    path('http404/', views.http404),
]
