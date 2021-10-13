from django.db import models
from django.shortcuts import render,redirect
from .import models
# Create your views here.


def readmakanan(req):
    if req.POST:
        input_jenis= req.POST["jenis"]
        input_name=req.POST["nama"]
        input_harga=req.POST["harga"]
        models.makanan.objects.create(jenis=input_jenis,nama=input_name,harga=input_harga)
      Data=models.makanan.objects.all()
      return render(req,"index.html",{
          "data":data, 
      })  