from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello alam , praxsis admin 2021. You're at the polls index.")