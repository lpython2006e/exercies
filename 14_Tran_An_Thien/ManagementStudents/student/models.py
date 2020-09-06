from django.forms import ModelForm, Textarea
from django.db import models


# from


# Create your models here.

class Class(models.Model):
    classname = models.CharField(max_length=100)
    type = models.CharField(max_length=20)


class Students(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    classname = models.ForeignKey(Class, on_delete=models.CASCADE, null=True)
