from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(unique=True, max_length=20)
    description = models.CharField(max_length=255)
    is_active = models.BooleanField()
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(unique=True, max_length=255)
    context = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    STATUS_DRAFT = 0
    STATUS_PUBLISHED = 100
    STATUS_REJECTED = 20
    STATUS_TRASHED = 25
    STATUS_AUTHCRIETED = 80
    STATUSES = (
        (STATUS_DRAFT, 'DRAFT'),
        (STATUS_PUBLISHED, 'DRAFT'),
        (STATUS_REJECTED, 'DRAFT'),
        (STATUS_TRASHED, 'DRAFT'),
        (STATUS_AUTHCRIETED, 'DRAFT'),
    )
    status = models.SmallIntegerField(choices=STATUSES, default=0)
