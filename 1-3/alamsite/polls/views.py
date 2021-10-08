# from typing_extensions import Required
from django.shortcuts import render, redirect
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

def hapus(request, id):
    models.tugas.objects.filter(id = id).delete()
    return redirect('/')

def edit(request, id):
    if request.POST:
        input = request.POST['nama']
        print(input)
        models.tugas.objects.filter(pk = id).update(nama = input)
        return redirect('/')

    hasil = models.tugas.objects.filter(pk = id).first()
    print(hasil)
    return render(request,'edit.html',{
        'detailedit' : hasil,

def detail(request, id):
    data = models.tugas.objects.filter(pk = id).first()
    print(data)
    return render(request,'detail.html',{
        "detailedit" :data 

    })