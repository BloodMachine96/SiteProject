from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Все прошло замечательно :)")

# Create your views here.
