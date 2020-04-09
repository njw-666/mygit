from django.shortcuts import render
import hashlib
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
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

## 登录装饰器
def loginValid(func):
    def inner(request,*args,**kwargs):
        ##校验登录
        cookie_email = request.COOKIES.get("buy_email")
        session_email = request.session.get("buy_email")
        if cookie_email and session_email and cookie_email == session_email:
            flag = LoginUser.objects.filter(email=cookie_email,id=request.COOKIES.get("buy_userid"),user_type=1).exists()
            if flag:
                return func(request,*args,**kwargs)
            else:
                return HttpResponseRedirect("/login/")
        else:
            return HttpResponseRedirect("/login/")
    return inner
# def loginValid(func):
#     def inner(request,*args,**kwargs):
#         cookie_email=request.COOKIES.get("buy_email")
#         session_email=request.session.get("buy_email")
#         if cookie_email and session_email and cookie_email == session_email:
#             return func(request,*args,**kwargs)
#         else:
#             return HttpResponseRedirect("/login/")
#     return  inner

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
    return render(request,"buyer/register.html")

def login(request):
    if request.method=="POST":
        print(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("pwd")
        if username and password:
             user=LoginUser.objects.filter(username=username,password=setPassword(password),user_type=1).first()
             if user:
                 response=HttpResponseRedirect("/")
                 response.set_cookie("buy_email",user.email)
                 response.set_cookie("buy_username", user.username)
                 response.set_cookie("buy_userid",user.id)
            # 区别：response用于设置cookie   request 用于设置session
            #      request.session["buy_username"]=user.username
                 request.session["buy_email"] = user.email

                 return  response
             else:
                 message="账号密码不正确"
        else:
             message="信息为空"

    return render(request, "buyer/login.html",locals())

#
@loginValid
def index(request):
    goods_type=GoodsType.objects.all()
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

    return render(request, "buyer/index.html",locals())


def logout(request):
    resp = HttpResponseRedirect("/login/")
    resp.delete_cookie("buy_email")
    resp.delete_cookie("buy_username")
    resp.delete_cookie("buy_userid")
    del request.session["buy_email"]
    return resp


def base(request):
    return render(request,"buyer/base.html")


def goods_list(request):
    kywards=request.GET.get("kywards")
    req_type=request.GET.get("req_type")
    if req_type=="find_all":
         goods_type=GoodsType.objects.filter(id=int(kywards)).first()
         goods=goods_type.goods_set.order_by("-goods_pro_time")
         print(goods)
    else:
        goods = Goods.objects.filter(goods_name__contains=kywards).order_by("-goods_pro_time")
    goods_new=goods[:2]
    return render(request,"buyer/goods_list.html",locals())


def goods_detail(request):
    ##    此方法好使   后边加  通过商品的i?goods_id=1d 获取商品 或者get 改为filter
    goods_id = request.GET.get("goods_id")
    goods = Goods.objects.get(id=int( goods_id))
    return render(request,"buyer/goods_detail.html",locals())

# uuid 唯一标识 作为id 几乎不会重复
def get_order_no():
    import uuid
    order_no=str(uuid.uuid4()).replace("-","")
    return order_no

@loginValid
def place_order(request):
    user_id=request.COOKIES.get("buy_userid")
    goods_id=request.GET.get("goods_id")
    goods_count= int(request.GET.get("goods_count"))
    goods = Goods.objects.get(id=goods_id)
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
    user_address=UserAddress.objects.filter(user_id=user_id,status=1).first()
    ## orderinfo
    return render(request, "buyer/place_order.html",locals())


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
    sum_goods=pay_order.orderinfo_set.aggregate(Sum("goods_count"),
                                                mycount=Count("id"))
    return render(request,"buyer/goods_test.html",locals())



## 支付宝支付  应该对
@loginValid
def alipay_order(request):
    ## 获取订单  payorder _id
    payorder_id = request.GET.get("payorder_id")
    payorder = PayOrder.objects.get(id=payorder_id)
    user_id=request.COOKIES.get("buy_user_id")
    user_address = UserAddress.objects.filter(user_id=user_id,status=1).first()
    payorder_address=PayorderAddress.objects.create(address=user_address.address,
                                                    phone=user_address.phone,
                                                    payorder=payorder

    )
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


#应该对
def pay_result(request):
    out_trade_no = request.GET.get("out_trade_no")
    ## 修改订单的状态  未付款 -》 已付款
    payorder = PayOrder.objects.get(order_number=out_trade_no)
    payorder.order_status = 2
    payorder.save()

    return render(request,"buyer/pay_result.html",locals())


#貌似没毛病
@loginValid
def cart(request):
    user_id = request.COOKIES.get("buy_userid")
    cart = Cart.objects.filter(cart_user=LoginUser.objects.get(id=int(user_id))).all()

    ## 获取购物车中所有商品的 小计之和 以及 商品的数量之和
    ## 聚合  all_total 字典  key：vlaue  ->  {"sum_total":3232,"sum_number":3232}
    all_total = cart.aggregate(sum_total=Sum("goods_total"), sum_number=Sum("goods_number"))

    return render(request, "buyer/cart.html", locals())

#貌似没毛病
@loginValid
def add_cart(request):
    result = {"code":10000,"msg":"添加购物车成功"}
    data = request.POST
    ## 从cookie中获取买家
    user_id = request.COOKIES.get("buy_userid")
    print(data)
    goods_id = data.get("goods_id")
    goods_count = int(data.get("goods_count",1))  ## 商品详情页
    goods = Goods.objects.get(id = goods_id)

    ## 判断购物车中是否已经存在该商品
    cart = Cart.objects.filter(goods = goods).first()
    if cart:
        ## 存在
        cart.goods_number += goods_count
        # cart.goods_total = goods.goods_price * (goods_count + cart.goods_number)
        cart.goods_total += goods.goods_price * goods_count
    else:
        ## 不存在
        cart = Cart()
        cart.goods = goods
        cart.goods_number = goods_count
        cart.goods_total = goods_count * goods.goods_price
        cart.cart_user_id = user_id
    try:
        cart.save()
        result = {"code":10000,"msg":"添加购物车成功"}
    except:
        result = {"code": 10001, "msg": "添加购物车失败"}
    return JsonResponse(result)

# def change_cart(request):
#     result={"code":1111,"msg":"计算失败","data":{}}
#     data=request.POST
#     print(data)
#     cart_id=request.POST.get("cart_id")
#     js_type=request.POST.get("js_type")
#     if cart_id and js_type:
#        cart=Cart.objects.filter(id=int(cart_id)).first()
#     if js_type=="add":
#         cart.goods_number +=1
#         cart.goods_total
#     return JsonResponse(result)
#貌似/没毛病
def change_cart(request):
    result = {"code":10001,"msg":"计算失败","data":{}}
    ## 修改购物车的数量 以及小计
    ##   购物车id
    ## 操作的类型    add reduce

    data= request.POST
    print(data)
    cart_id = request.POST.get("cart_id")
    js_type = request.POST.get("js_type")
    if cart_id and js_type:
        cart = Cart.objects.filter(id = int(cart_id)).first()
        if cart:
            if js_type == "add":
                ## 加 操作
                cart.goods_number += 1
                cart.goods_total += cart.goods.goods_price
            else:
                ##减操作
                cart.goods_number -= 1
                cart.goods_total -= cart.goods.goods_price
            try:
                cart.save()
                result = {"code":10000,"msg":"操作成功","data":{"goods_number":cart.goods_number,"goods_total":cart.goods_total}}
            except:
                result = {"code":10003,"msg":"操作失败"}

        ## 将修改之后结果 返回到前端
        else:
            result = {"code": 10002, "msg": "商品不存在", "data": {}}

    return JsonResponse(result)


#貌似没毛病
@loginValid
def cart_place_order(request):
    ## 获取购物车 id
    data = request.POST
    res = []   ### 购物车id
    for key,value in data.items():
        # print(key)
        # print(value)
        if key.startswith("cart_id"):
            res.append(value)
    print(res)
    ## 将购物中选中的商品 生成订单
    user_id = request.COOKIES.get("buy_userid")
    ## 查找商品
    ##payorder
    payorder = PayOrder()
    payorder.order_number = get_order_no()
    payorder.order_status = 1   ### 未支付状态
    payorder.order_total = 0   ## 订单总价  =  订单详情中的小计的和
    payorder.order_user_id = int(user_id)
    payorder.save()

    ### 生成订单详情
    for one in res:
        ## 查找购物车
        cart = Cart.objects.filter(id =one).first()
        order_info = OrderInfo()
        order_info.order = payorder
        order_info.goods = cart.goods
        order_info.goods_price = cart.goods.goods_price
        ## 店铺的信息 通过商品寻找 店铺
        order_info.store = cart.goods.goods_store
        order_info.goods_count = cart.goods_number
        order_info.goods_total_price = cart.goods_total
        order_info.save()
        cart.delete()

    payorder_total = payorder.orderinfo_set.aggregate(sum_total = Sum("goods_total_price")).get("sum_total")
    payorder.order_total = payorder_total
    payorder.save()

    return render(request,"buyer/place_order.html",locals())


@loginValid
def user_center_info(request):
    buy_userid=request.COOKIES.get("buy_userid")
    user=LoginUser.objects.filter(id=buy_userid).first()

    return render(request,"buyer/user_center_info.html",locals())


def user_center_order(request):
    return render(request,"buyer/user_center_order.html",locals())

@loginValid
def user_center_site(request):
    ## get请求   获取当前的地址
    buy_userid = request.COOKIES.get("buy_userid")
    user = LoginUser.objects.filter(id=buy_userid).first()
    # useraddress = UserAddress.objects.filter(user=user).first()

    ## post请求   提交新的地址
    if request.method == "POST":
        print(request.POST)
        data = request.POST
        UserAddress.objects.create(name=data.get("name"),
                                   address=data.get("address"),
                                   phone=data.get("phone"),
                                   user=user
                                   )
    useraddress = UserAddress.objects.filter(user=user).all()
    return  render(request,"buyer/user_center_site.html",locals())



@loginValid
def update_useraddress(request):
    if request.method == "POST":
        data = request.POST
        address_id = request.POST.get("address")
        buy_userid = request.COOKIES.get("buy_userid")
        user = LoginUser.objects.filter(id=buy_userid).first()
        print(data)
        ## 修改用户地址的状态
        ## 将之前的地址状态  改为 0
        UserAddress.objects.filter(user=user).update(status=0)
        ## address_id 地址修改为当前使用的地址  改为1
        UserAddress.objects.filter(id=address_id).update(status=1)
    return HttpResponseRedirect("/buyer/user_center_site/")



