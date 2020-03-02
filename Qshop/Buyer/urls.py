from .views import  *
from django.urls import path,re_path,include
urlpatterns = [
path("index/",index),
path("register/",register),
path("login/",login),
path("logout/",logout),
path("base/",base),
path("goods_list/",goods_list),
path("goods_detail/",goods_detail),
path("place_order/",place_order),
path("gettest/",gettest),
path("goods_test/",goods_test),
path("pay_result/",pay_result),
path("alipay_order/",alipay_order),



]