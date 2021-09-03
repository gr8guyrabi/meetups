from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Every view is a function to be called.


def index(request):
    return HttpResponse('Hello World!')
