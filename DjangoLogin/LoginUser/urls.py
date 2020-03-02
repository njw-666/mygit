# from django.contrib import admin
from django.urls import path,re_path
from LoginUser.views import *
from rest_framework.routers import SimpleRouter
router=SimpleRouter()   #先实例化一个对象  将视图进行一个注册
router.register(r"API/Goods",GoodsViews)  #加S和不加区别不一样的 Goods View 在这里是错误的

urlpatterns = [
    path("goods_list/",goods_list),
    path("add_goods/",add_goods),
    # re_path("goods_list/(?P<page>\d+)/",goods_list),
    re_path("goods_list/(?P<page>\d+)/(?P<status>\d+)/",goods_list),
    re_path("goods_status/(?P<id>\d+)/(?P<status>\w+)/",goods_status),
    re_path("goods_list_api/(?P<page>\d+)/(?P<status>\d+)/",goods_list_api),
    path("goods_list_ajax/", goods_list_ajax),
    path("rase_vue/",rase_vue),

]
#     # path('admin/', admin.site.urls),
#     path("register/",register),
#     path("login/",login),
#     re_path("^$",index),
#     path("index/",index),
# ]