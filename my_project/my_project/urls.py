"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url


from my_app import views
from my_app.views import IndexView, TaskListView, TaskDetailView, TaskFormView


urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^tasks/$', IndexView.as_view()),
    url(r'^tasks/$', TaskListView.as_view(template_name="my_app/index.html")),
    url(r'^tasks/create$', TaskFormView.as_view()),
    # url(r'^tasks/<pk>$', UpdateView.as_view()),
    # url(r'^tasks/<pk>/delete$', DeleteView.as_view()),
    # url(r'^tasks/add$', CreateView.as_view()),
    url(r'^tasks/(?P<pk>[0-9a-f\-]+)$', TaskDetailView.as_view(template_name="my_app/detail.html")),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
