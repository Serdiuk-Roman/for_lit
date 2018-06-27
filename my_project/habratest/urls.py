from django.conf.urls import url

from habratest.views import Posts, PostsIndex


# Укажем дополнительный маршрут,
# чтобы главная страница была доступна без указания номера страницы
urlpatterns = [
    # Отдельный список статей для главной страницы
    # (рейтинг которых выше, либо равен, 10)
    url(r'^$', PostsIndex.as_view()),
    url(r'^page(?P<page>\d+)/$', PostsIndex.as_view()),

    # Список всех активных статей
    url(r'^posts/$', Posts.as_view()),
    url(r'^posts/page(?P<page>\d+)/$', Posts.as_view()),
]
