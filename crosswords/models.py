from django.db import models


# Create your models here.
class Crossword(models.Model):
    code = models.CharField(max_length=10000000000)
