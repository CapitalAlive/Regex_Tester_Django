from django.db import models


# Create your models here.
class Record(models.Model):
    regex = models.CharField(max_length=50)
    text = models.TextField(max_length=1024)
    result = models.BooleanField()
