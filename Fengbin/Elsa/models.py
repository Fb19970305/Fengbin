# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Elsa(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=255, default="")
    urls = models.TextField(default="")
    price = models.DecimalField(max_digits=4, decimal_places=2)
    cloth_type = models.IntegerField(default=0)
    cloth_num = models.IntegerField(default=0)

    class Meta:
        db_table = 'elsa'