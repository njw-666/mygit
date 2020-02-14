# from django.contrib import admin
from django.urls import path,re_path
from.views import *
# from app01 import views as app01_views
urlpatterns = [
path("index/",index),
    path("about/",about),
]