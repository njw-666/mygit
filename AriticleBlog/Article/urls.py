from django.urls import path,re_path
from.views import *
urlpatterns = [
    path("index/", index),
    path("about/", about, name="myabout"),
    path("listpic/", listpic),
    path("newslistpic/", newslistpic),
    path("base/",base),
]

