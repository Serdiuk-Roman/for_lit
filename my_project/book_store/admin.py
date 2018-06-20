from django.contrib import admin

# Register your models here.

from .models import Author, Book, Tag, BookTags

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Tag)
admin.site.register(BookTags)
