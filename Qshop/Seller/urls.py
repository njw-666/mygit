from django.urls import path,re_path
from .views import *

urlpatterns = [
path("goods_list/",goods_list),
re_path("goods_list/(?P<page>\d+)/(?P<status>\d+)/",goods_list),
re_path("goods_status/(?P<id>\d+)/(?P<status>\w+)/",goods_status),
path("base/",base),
path("loginout/", loginout),
# path("loginuser/", loginuser),
path("register/",register),
path("login/",login),
path("index/",index),
path("user_profile/",user_profile),
path("goods_add/",goods_add),
# path("add_label/",add_label),
]
