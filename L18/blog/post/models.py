from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(unique=True, max_length=20)
    description = models.CharField(max_length=255)
    is_active = models.BooleanField()
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


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
        (STATUS_PUBLISHED, 'PUBLISHED'),
        (STATUS_REJECTED, 'REJECTED'),
        (STATUS_TRASHED, 'TRASHED'),
        (STATUS_AUTHCRIETED, 'AUTHCRIETED'),
    )
    status = models.SmallIntegerField(choices=STATUSES, default=0)

    def __str__(self):
        return self.title
