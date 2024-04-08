from django.shortcuts import render

from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.
