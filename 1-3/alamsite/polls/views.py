from django.shortcuts import render 
from . import models
# Create your views here.
from django.http import HttpResponse


def index(request):
    if request.POST:
        input=request.POST["nama"]
        models.tugas.objects.create(nama=input)
    data=models.tugas.objects.all()
        
    return render(request,'index.html',{
        "data":data
    })