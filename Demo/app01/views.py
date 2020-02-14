from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("这是子应用app01的index视图哦")

def about(request):
    return HttpResponse("这是子应用的about页面")