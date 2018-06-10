#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.db import models


class Shortly(models.Model):
    url_id = models.AutoField(primary_key=True)
    url_target = models.URLField(max_length=250, unique=True)
    click_count = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = 'Url'
        verbose_name_plural = 'Urls'
