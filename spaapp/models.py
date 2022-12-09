from django.db import models


# Create your models here.
class Membership(models.Model):
    name = models.CharField(max_length=150)
    validity = models.IntegerField()
    desc = models.CharField(max_length=200)
