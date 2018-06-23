from django.contrib import admin

# Register your models here.

from shortly_app.models import Snippet, Shortly

admin.site.register(Snippet)
admin.site.register(Shortly)
