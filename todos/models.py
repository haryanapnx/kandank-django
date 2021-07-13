from django.db import models

# Create your models here.


class Todos(models.Model):
    name = models.CharField(default='', max_length=225)
    description = models.TextField()
