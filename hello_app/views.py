from django.shortcuts import render

# Create your views here.
import django.http
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello, World!')
