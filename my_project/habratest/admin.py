from django.contrib import admin

from habratest.models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'created_at')


admin.site.register(Post, PostAdmin)
