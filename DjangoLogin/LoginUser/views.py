from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from .models import LoginUser,Goods
from django.core.paginator import Paginator
import hashlib
from django .views import View

# Create your views here.
def setPassword(password):
    md5=hashlib.md5()
    md5.update(password.encode())
    result=md5.hexdigest()
    return result

def set_session(request):
    # username=request.get("username")
    # print(username)
    return HttpResponse("设置session")

#登录装饰器
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
    print(request.POST)
    password=request.POST.get("password")
    repassword = request.POST.get("repassword")
    email = request.POST.get("email")
    if email and password and password ==repassword:
        LoginUser.objects.create(email=email,password=password)
        return HttpResponseRedirect("/login/")
    else:
        message="参数为空"
    return render(request,"register.html",locals())

def login(request):
    if request.method=="POST":
        print(request.POST)
        email = request.POST.get("email")
        password = request.POST.get("password")
        if email and password:
             user=LoginUser.objects.filter(email=email,password=setPassword(password)).first()
             if user:
                 response=HttpResponseRedirect("/")
                 response.set_cookie("email",user.email)
            # 区别：response用于设置cookie   request 用于设置session
                 request.session["email"]=user.email

                 return  response
             else:
                 message="账号密码不正确"
        else:
             message="信息为空"

    return render(request, "login.html",locals())


@loginValid
def index(request):
    # return HttpResponse("index")
    return render(request,"index.html")




def base(request):
    return render(request,"base.html")


def loginout(request):
    response=HttpResponseRedirect("/login/")
    response.delete_cookie("email")
    del request.session["email"]
    return response



# def goods_list(request):
#     return render(request,"goods_list.html")


# import random
# ## 添加 100 商品
def add_goods(request):
#     ## 循环
#     goods_name = "萝卜、马铃薯、藕、甘薯、山药、芋头、茭白、苤蓝、慈姑、洋葱、生姜、大蒜、蒜薹、韭菜花、大葱、韭黄、冬瓜、南瓜、西葫芦、丝瓜、黄瓜、茄子、西红柿、苦瓜、辣椒、玉米、小瓜、菠菜、油菜、卷心菜、苋菜、韭菜、蒿菜、香菜、芥菜、芥兰"
#     goods_name = goods_name.split("、")
#     goods_address = "石家庄、沈阳、哈尔滨、杭州、福州、济南、广州、武汉、成都、昆明、兰州、台北、南宁、银川、太原、长春、南京、合肥、南昌、郑州、长沙、海口、贵阳、西安、西宁、呼和浩特、拉萨、乌鲁木齐"
#     goods_address = goods_address.split("、")
#     for i,j in enumerate(range(100),1):
#         goods = Goods()
#         # goods_number 为  00001    00002   00100
#         goods.goods_number = str(i).zfill(5)
#         goods.goods_name  = random.choice(goods_address)+random.choice(goods_name)
#         goods.goods_price = round(random.random()*100,2)  ## 保留小数点 2位
#         goods.goods_count = random.randint(1,100)    ##
#         goods.goods_location = random.choice(goods_address)
#         goods.goods_safe_date = random.randint(1,32)
#         goods.save()
    return HttpResponse("add goods")

@loginValid
def goods_list(request,status,page=1):
    # goods=Goods.objects.all()
    goods=Goods.objects.first(goods_status=status).order_by("id")
    goods_obj=Paginator(goods,10)
    goods_list=goods_obj.page(page)
    # return render(request,"goods_list.html",locals())
    return render(request,"goods_list_vue.html")

def goods_status(request,id,status):
    goods=Goods.objects.get(id=id)
    if status =="up":
        goods.goods_status=1
        goods.save()
    else:
        goods.good_status=0
        goods.save()
        url = request.META.get("HTTP_REFERER") #得到请求的地址
    return HttpResponseRedirect(url) # 重定向到请求的地址
    # return HttpResponseRedirect("/loginuser/goods_list/1/1/")  # 先完成这个 再完成url



# 视图：  只提供数据
def goods_list_api(request,status,page=1):
    goods = Goods.objects.filter(goods_status=status).order_by("id")
    goods_obj = Paginator(goods,8)
    goods_list = goods_obj.page(page)
    result = {"code":10000,"msg":"成功","data":""}
    res = []
    for one in goods_list:
        res_dict = {
            "id":one.id,
	            "goods_number":one.goods_number,
	            "goods_name":one.goods_name,
	            "goods_price":one.goods_price,
                "goods_count":one.goods_count,
                "goods_location":one.goods_location,
                "goods_safe_date":one.goods_safe_date,
	            "goods_status":one.goods_status,}
        res.append(res_dict)
    result["data"] = res
    result["page"]=page
    result["page_range"] = list(goods_obj.page_range)
    # return JsonResponse(result)
    response=JsonResponse(result)
    response["Access-Control-Allow-Origin"] = "*"     #添加允许访问的主机和域名
    return response   #解决跨域请求


def goods_list_ajax(request):
    return render(request,"ajax_goods_list.html")







# 2月24日第三阶段第十一天学习代码如下:
def rase_vue(request):
    return render(request,"rase_vue.html",locals())

# 类似图支持的请求方式：
# http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']


class GoodsView(View):
    def __init__(self):
        super(GoodsView,self).__init__()
        self.result={
            "version":"",
            "methon":"",
            "data":"",
            "mst":"",
            "code":"",
        }
        self.obj=Goods
    def get(self,request):
        # result = {"methods": "get请求"}
        id =request.GET.get("id")
        if id:
            # goods=Goods.objects.filter(id=id).first()
            goods = self.obj.objects.filter(id=id).first()
            data={
                "goods_number": goods.goods_number,
                "goods_name": goods.goods_name,
                "goods_price": goods.goods_price,
                "goods_count": goods.goods_count,
                "goods_location": goods.goods_location,
                "goods_safe_date": goods.goods_safe_date,
                "goods_status": goods.goods_status,

            }
            # result["data"]=data
        else:
             # goods=Goods.objects.all()
             goods = self.obj.objects.all()
             data=[]
             for one in goods:
                res={
                "goods_number": one.goods_number,
                "goods_name": one.goods_name,
                "goods_price": one.goods_price,
                "goods_count": one.goods_count,
                "goods_location":one.goods_location,
                "goods_safe_date": one.goods_safe_date,
                "goods_status": one.goods_status,

                }
                data.append(res)
                # result["data"]=data
        self.result["methods"] = "get请求"
        self.result["data"] = data
        self.result["code"] = 10000
        self.result["msg"] = "请求成功"

        return JsonResponse(self.result)
    # 处理post请求  提交数据
    def post(self, request):
        # 提交数据，保存数据
        data = request.POST
        goods = Goods()
        goods.goods_number = data.get("goods_number")
        goods.goods_name = data.get("goods_name")
        goods.goods_price = data.get("goods_price")
        goods.goods_count = data.get("goods_count")
        goods.goods_location = data.get("goods_location")
        goods.goods_safe_date = data.get("goods_safe_date")
        goods.save()

        self.result["methods"] = "post请求"
        self.result["data"] = {"id": goods.id}
        self.result["code"] = 10000
        self.result["msg"] = "保存数据成功"
        return JsonResponse(self.result)

        ## 处理put请求

    def put(self,request):

        ## 获取id
        ##  put 请求参数如何获取，不在GET中，也不在post而是在body中
        import json
        # date = request.body    ## b''   b'{"id":1}'   bytes
        # ## 将bytes 类型 转化为 string
        # date = date.decode()
        # print(date)
        # data = json.loads(date)
        # print(data)
        # id = data.get("id")
        # print(id)
        date = json.loads(request.body.decode())
        # 需求： 通过id 修改某个商品的名字
        id = date.get("id")
        goods_name = date.get("goods_name")
        # 判断
        flag = Goods.objects.filter(id=id).exists()
        if flag:
            ## 存在
            ## 修改
        #     Goods.objects.filter(id=id).update(goods_name=goods_name)
        #
            self.result["methods"] = "put请求"
            self.result["data"] = {"id": id}
            self.result["code"] = 10000
            self.result["msg"] = "修改数据成功"
        else:
        # #     ## 不存在
            self.result["methods"] = "put请求"
            self.result["data"] = {"id": id}
            self.result["code"] = 10001
            self.result["msg"] = "商品不存在"
        # result = {"methods": "put请求"}
        return JsonResponse(self.result)

        ## 处理delete 请求你
    def delete(self, request):
        import json
        date=json.loads(request.body.decode())
        id = date.get("id")
        Goods.objects.filter(id=id).delete()
        result = {"methods": "delete请求"}
        self.result["data"] = {"id": id}
        self.result["code"] = 10000
        self.result["msg"] = "商品删除成功"
        return JsonResponse(self.result)



from django.middleware.csrf import get_token
def gettoken(request):
    token = get_token(request)
    return JsonResponse({"token":token})


from .serializers import GoodsSerializers
from rest_framework import mixins,viewsets
class GoodsViews(mixins.CreateModelMixin,   #创建
                 mixins.UpdateModelMixin,    #更新
                 mixins.DestroyModelMixin,    #删除
                 mixins.ListModelMixin,       # 列表
                 mixins.RetrieveModelMixin,   # 检索
                 viewsets.GenericViewSet):     # rest的基类
    queryset = Goods.objects.all()   #返回的数据
    serializer_class = GoodsSerializers

