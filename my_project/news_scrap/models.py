from django.db import models

# Create your models here.


class ShortNews(models.Model):
    news_link = models.URLField()
    title = models.CharField(max_length=128)
    img = models.FileField()
    lid = models.TextField()
    author = models.CharField(max_length=64)
    date = models.DateTimeField()

    class Meta:
        verbose_name = 'news'
