from django.db import models

# Create your models here.


class BookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(author__isnull=False)

    def with_tag(self, tag):
        return self.get_queryset().filter(tags__name=tag)


class Author(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(
        Author,
        models.CASCADE,  # CASCADE, SET_NULL, PROTECT, SET_DEFAULT, DO_NOTHING
        related_name='books',
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='bkj'
    )
    tags2 = models.ManyToManyField(
        Tag,
        through='BookTags',
        related_name='bkjaaaaaaaaa'
    )

    def __str__(self):
        return self.title + '<=>' + self.author.name

    with_author = BookManager()


class BookTags(models.Model):
    book = models.ForeignKey(Book, models.CASCADE)
    tag = models.ForeignKey(Tag, models.CASCADE, related_name='booktags')

