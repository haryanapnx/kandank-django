from django.db import models
from django.db.models.aggregates import Max


class Tutorial(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description= models.TextField()
    published = models.BooleanField(default=False)
