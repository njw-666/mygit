from django.urls import path,re_path
from . views import *

urlpatterns = [
    path("adduser/",adduser),
    path("getuser/",getuser),
    path("update_user/",update_user),
    path("delete_user/",delete_user),
    path("doubleline/",doubleline),
    path("add_f/",add_f),
    path("get_f/",get_f),
    path("update_f/",update_f),
    path("delete_f/",delete_f),
    path("about/",about ,name="myabout"),
    path("index/",index),
    path("listpic/",listpic),
    re_path("newslistpic/(?P<page>\d+)/",newslistpic),
    path("newslistpic/",newslistpic),
    path("choices_test/",choices_test),
    path("article_p/",article_p),
    path("add_article/",add_article),
    path("indexxx/",indexxx),
    # path("getdemo/",getdemo),
    # path ("register/",register),
    # path("ajax_post_req/",ajax_post_req),
    path("ajax_get_req/",ajax_get_req),
    path("ajaxdemo/",ajaxdemo),
    path("set_cookie/",set_cookie),
    path("get_cookie/",get_cookie),
    path("delete_cookie/",delete_cookie),
    path("set_session/",set_session),
    path("set_session/",set_session),
    path("get_session/",get_session),
    path("delete_session/",delete_session),
    path("rase_vue/",rase_vue),



]