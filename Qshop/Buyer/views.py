from django.shortcuts import render
import hashlib
from django.http import HttpResponse,HttpResponseRedirect
from Seller.models import *
from .models import *
from django .db.models import Sum,Count,Max,Min,Avg
from Qshop.settings import alipay
# Create your views here.
def setPassword(password):
    md5=hashlib.md5()
    md5.update(password.encode())
    result=md5.hexdigest()
    return result
def loginValid(func):
    def inner(request,*args,**kwargs):
        cookie_email=request.COOKIES.get("email")
        session_email=request.session.get("email")
        if cookie_email and session_email and cookie_email == session_email:
            return func(request,*args,**kwargs)
        else:
            return HttpResponseRedirect("/login/")
    return  inner

def register(request):
    if request.method == "POST":
        # print(request.POST)
        username=request.POST.get("user_name")
        password=request.POST.get("pwd")
        repassword = request.POST.get("cpwd")
        email = request.POST.get("email")
        if email and password and password ==repassword:
            LoginUser.objects.create(email=email,password=setPassword(password),username= username)
            return HttpResponseRedirect("/login/")
        else:
            message="参数为空"
    return render(request,"Buyer/register.html")

def login(request):
    if request.method=="POST":
        print(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("pwd")
        if username and password:
             user=LoginUser.objects.filter(username=username,password=setPassword(password),user_type=1).first()
             if user:
                 response=HttpResponseRedirect("/index/")
                 response.set_cookie("buy_email",user.email)
                 response.set_cookie("buy_username", user.username)
                 response.set_cookie("buy_userid",user.id)
            # 区别：response用于设置cookie   request 用于设置session
                 request.session["buy_username"]=user.username

                 return  response
             else:
                 message="账号密码不正确"
        else:
             message="信息为空"

    return render(request, "Buyer/login.html",locals())

#
# @loginValid
def index(request):
    goods_type=Goods.objects.all()
    print((goods_type))
    # res = [{"type": "新鲜水果.obj", "goods": [goods1, goods2, goods3, goods4]}, {}, {}]
    res=[]
    for one in goods_type:
        print(one)
        goods = one.goods_set.order_by("id").all()
        if len(goods) > 4:
            goods_list = goods[:4]
            res.append({"type": one, "goods_list": goods_list})
        elif len(goods) > 0 and len(goods) <= 4:
            goods_list = goods
            res.append({"type": one, "goods_list": goods_list})
        print(res)

    return render(request, "Buyer/index.html",locals())


def logout(request):
    resp = HttpResponseRedirect("/login/")
    resp.delete_cookie("email")
    resp.delete_cookie("username")
    resp.delete_cookie("userid")
    del request.session["email"]
    return resp


def base(request):
    return render(request,"buyer/base.html")


def goods_list(request):
    kywards=request.GET.get("kywards")
    req_type=request.GET.get("req_type")
    if req_type=="find_all":
         goods_type=GoodsType.objects.filter(id=kywards).first()
         goods=goods_type.goods_set.order_by("-goods_pro_time")
         print(goods)
    else:
        goods = Goods.objects.filter(goods_name__contains=kywards).order_by("-goods_pro_time")
        goods_new=goods[:2]
    return render(request,"buyer/goods_list.html",locals())


def goods_detail(request):
    ##    此方法好使   后边加  通过商品的i?goods_id=1d 获取商品 或者get 改为filter
    goods_id = request.GET.get("goods_id")
    goods = Goods.objects.get(id= goods_id)
    return render(request,"buyer/goods_detail.html",locals())

# uuid 唯一标识 作为id 几乎不会重复
def get_order_no():
    import uuid
    order_no=str(uuid.uuid4()).replace("-","")
    return order_no

# @loginValid
def place_order(request):
    user_id=request.COOKIES.get("buy_userid")
    goods=request.GET.get("goods_id")
    goods_count= int(request.GET.get("goods_count"))
    # goods = Goods.objects.get(id=goods_id)
    payorder = PayOrder()
    payorder.order_number=get_order_no()
    payorder.order_status =1
    payorder.order_total=goods_count *goods.goods_price
    payorder.order_user_id = int(user_id)
    payorder.save()




    order_info = OrderInfo()
    order_info.order = payorder
    order_info.goods = goods
    order_info.goods_price = goods.goods_price
    ## 店铺的信息 通过商品寻找 店铺
    order_info.store = goods.goods_store
    order_info.goods_count = goods_count
    order_info.goods_total_price = goods_count * goods.goods_price
    order_info.save()

    ## orderinfo
    return render(request, "buyer/place_order.html",locals)


def gettest(request):
    payorder=PayOrder.objects.get(id=1)
    order_info=payorder.orderinfor_set.first()
    goods=order_info.goods
    print(goods.goods_name)

    goods_name=payorder.orderinfor_set.first().goods.goods_name
    print (goods_name)


    return HttpResponse("test")

def goods_test(request):
    order_id = 1
    pay_order=PayOrder.objects.get(id=order_id)
    # 聚合方法aggregate  返回值 字典  key默认值  goods_count聚合方法
    sum_goods=pay_order.orderinfo_set.aggregate(Sum("goods_count"),mycount=Count("id"))
    return render(request,"buyer/goods_test.html",locals())



## 支付宝支付
def alipay_order(request):
    ## 获取订单  payorder _id
    payorder_id = request.GET.get("payorder_id")
    payorder = PayOrder.objects.get(id=payorder_id)
    # 3、 实例化一个订单
    order_string = alipay.api_alipay_trade_page_pay(
        subject="生鲜交易",  ## 主题
        out_trade_no= payorder.order_number,  ## 订单号
        total_amount= str(payorder.order_total),  ## 交易金额   字符串
        # return_url=None,  ##  回调的地址
        return_url="http://127.0.0.1:8000/buyer/pay_result/",
        notify_url=None  ## 通知
    )

    # 4、 返回支付宝支付的url
    result = "https://openapi.alipaydev.com/gateway.do?" + order_string
    return HttpResponseRedirect(result)



def pay_result(request):
    out_trade_no = request.GET.get("out_trade_no")
    ## 修改订单的状态  未付款 -》 已付款
    payorder = PayOrder.objects.get(order_number=out_trade_no)
    payorder.order_status = 2
    payorder.save()

    return render(request,"buyer/pay_result.html",locals())


