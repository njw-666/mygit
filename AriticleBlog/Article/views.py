from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect

# from .urls import *
def index(rquest):
    return render_to_response("index.html")
def about(request):
    return render_to_response("about.html")
def listpic(request):
    return render_to_response("listpic.html")
def newslistpic(request):
    return render_to_response("newslistpic.html")
def base(request):
    return render_to_response("base.html")


