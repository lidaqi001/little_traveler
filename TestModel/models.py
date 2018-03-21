from django.db import models


# Create your models here.

class Test(models.Model):
    name = models.CharField(max_length=20)


class User(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
