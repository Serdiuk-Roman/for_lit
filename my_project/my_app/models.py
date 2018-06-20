from django.db import models
import uuid

# Create your models here.


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    text = models.CharField(max_length=64)
    checked = models.BooleanField(
        # null=True,
        # blank=True,
        # default=False,
        # verbose_name='Check',
        # unique=False
        # validators=...
    )

    class Meta:
        verbose_name = 'one name'
        verbose_name_plural = 'plural name'
