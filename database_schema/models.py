from __future__ import unicode_literals

from django.db import models
import datetime

class Product(models.Model):
    sku = models.IntegerField(max_length=50)
    description = models.TextField(max_length=50)
    store_id = models.IntegerField(max_length=50)
    is_promotion = models.BooleanField(default=False)
    sku = models.CharField(max_length=50)
    created = datetime

    def save(self,*args, **kwargs):
        if not kwargs.get('force_insert') and self.created is None:
            self.created = datetime.datetime.utcfromtimestamp(0)
        super(Product, self).save(*args, **kwargs)
