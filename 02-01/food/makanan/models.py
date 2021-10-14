from django.db import models
from django.db.models.fields import CharField
from django.http.response import JsonResponse

# Create your models here.

class makanan(models.Model):
    jenis=models.CharField(default='', max_length=10)
    nama=models.CharField(default='', max_length=15)
    harga=models.IntegerField()