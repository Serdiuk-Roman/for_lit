from django.conf.urls import url
from news_scrap.views import NewsListView, NewsDetailView, NewsFormView

urlpatterns = [
    url(r'', NewsListView.as_view()),
    url(r'create$', NewsFormView.as_view(), name="news_post"),
    url(r'(?P<pk>[0-9a-f\-]+)$',
        NewsDetailView.as_view(template_name="my_app/detail.html")),
]


# celery sheduling
# http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html
