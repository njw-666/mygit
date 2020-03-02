from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from .models import LoginUser,Goods,GoodsType
from django.core.paginator import Paginator
import hashlib
from django .views import View

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
            return HttpResponseRedirect("/seller/login/")
    return  inner



def register(request):
    if request.method == "POST":
        # print(request.POST)
        password=request.POST.get("password")
        repassword = request.POST.get("repassword")
        email = request.POST.get("email")
        if email and password and password ==repassword:
            LoginUser.objects.create(email=email,password=setPassword(password),user_type=0)
            return HttpResponseRedirect("/seller/login/")
        else:
            message="参数为空"
    return render(request,"seller/register.html",locals())

def login(request):
    if request.method=="POST":
        print(request.POST)
        email= request.POST.get("email")
        password = request.POST.get("password")
        if email and password:
             user=LoginUser.objects.filter(email=email,password=setPassword(password),user_type=0).first()
             if user:
                 response=HttpResponseRedirect("/seller/index/")
                 response.set_cookie("email",user.email)
                 response.set_cookie("userid", user.id)
            # 区别：response用于设置cookie   request 用于设置session
                 request.session["email"]=user.email

                 return  response
             else:
                 message="账号密码不正确"
        else:
             message="信息为空"

    return render(request, "seller/login.html",locals())


@loginValid
def index(request):
    # return HttpResponse("index")
    return render(request,"seller/index.html")




def base(request):
    return render(request,"seller/base.html")

def loginout(request):
    response=HttpResponseRedirect("/seller/login/")
    response.delete_cookie("email")
    del request.session["email"]
    return response



@loginValid
def goods_list(request,status,page=1):
    # goods=Goods.objects.all()
    goods=Goods.objects.filter(goods_status=status,goods_store_id=request.COOKIES.get("userid")).order_by("id")
    goods_obj=Paginator(goods,10)
    goods_list=goods_obj.page(page)
    # return render(request,"goods_list.html",locals())
    return render(request,"seller/goods_list.html",locals())

def goods_status(request,id,status):
    goods=Goods.objects.get(id=id)
    if status =="up":
        goods.goods_status=1
        goods.save()
    else:
        goods.good_status=0
        goods.save()
    url = request.META.get("HTTP_REFERER") #得到请求的地址
    print(url)
    return HttpResponseRedirect(url) # 重定向到请求的地址
    # return HttpResponseRedirect("/loginuser/goods_list/1/1/")  # 先完成这个 再完成url




@loginValid
def user_profile(request):
    ## 返回用户的信息
    ## 从session 或者 cokkie 这种获取登录的用户
    userid = request.COOKIES.get("userid")
    user = LoginUser.objects.get(id=userid)
    ## 处理post请求
    if request.method == "POST":
        date = request.POST
        user.email = date.get("email")
        user.phone_number = date.get("phone_number")
        user.username = date.get("username")
        user.age = date.get("age")
        user.gender = date.get("gender")
        user.address = date.get("address")
        # if request.FILES.get("img"):
        user.photo = request.FILES.get("img")
        user.save()
        return render(request,"seller/user_profile.html")


def add_label(request):
    GoodsType.objects.create(type_label="新鲜水果",type_description="新鲜水果",type_picture="img/banner01.jpg")
    GoodsType.objects.create(type_label="海鲜水产",type_description="海鲜水产",type_picture="img/banner02.jpg")
    GoodsType.objects.create(type_label="猪牛羊肉",type_description="猪牛羊肉",type_picture="img/banner03.jpg")
    GoodsType.objects.create(type_label="禽类蛋品",type_description="禽类蛋品",type_picture="img/banner04.jpg")
    GoodsType.objects.create(type_label="新鲜蔬菜",type_description="新鲜蔬菜",type_picture="img/banner05.jpg")
    GoodsType.objects.create(type_label="速冻食品",type_description="速冻食品",type_picture="img/banner06.jpg")
    return HttpResponse("类型")



def goods_add(request):
    goods_type=GoodsType.objects.all()
    if request.method == "POST":
      user_id=request.COOKIES.get("userid")
      data=request.POST
      goods = Goods()
      goods.goods_number=data.get("goods_number")
      goods.goods_name = data.get("goods_name")
      goods.goods_price = data.get("goods_price")
      goods.goods_count = data.get("goods_count")
      goods.goods_location = data.get("goods_location")
      goods.goods_safe_date = data.get("goods_safe_date")
    # goods.goods_picture = data.get("goods_number")
      goods.goods_type_id = int(data.get("goods_type"))
      goods.goods_store = LoginUser.objects.get(id=user_id)
      goods.goods_picture = request.FILES.get("img")
      goods.save()

    return render(request, 'seller/goods_add.html', locals())




