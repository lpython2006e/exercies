from django.db import models


class Class(models.Model):
    classname = models.CharField(max_length=100)
    type = models.CharField(max_length=20)
