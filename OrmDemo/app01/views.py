from django.shortcuts import render,render_to_response
import hashlib
from django.http import  JsonResponse
# Create your views here.
from django.core.paginator import Paginator
from django.http import HttpResponse
from.models import *
from django.http import HttpResponseRedirect


def adduser(request):
    #orm 操作  增加 第一种  save()方法
    # 先实例化对象
    # user=User()
    # 逐个对属性进行赋值
    # user.user_name="小 吴"
    # user.age=20
    # user.phone="13456786789"
    # user.email="xiaowu.163.com"
    # user.save()
    # 第二种
    # user = User(user_name="小张", age=20, phone="15201010101", email="xiaozhang@126.com")
    # user.save()


    ## create
     ## 1.能够增加数据
     ## 2.会将增加的当条数据 返回

     # create方法
    # User.objects.create(user_name="laoliu", age=21, phone="15201010103", email="laoliu@126.com")
    # ## 第二种 字典
    # params = dict(user_name="laopo", age=22, phone="15201010100", email="laopo@126.com")
    # User.objects.create(**params)  ## 解包
    # User.objects.create({"user_name":"laob"})有瑕疵  没体验
    # return HttpResponse("添加数据")


    # get()方法  只返回符合条件的对象，可以是姓名年龄和id等字段条件，如对象不存在则会报错
    # user=User.objects.get(age=25 )#name="",id=
    # print(user)


     # 1.  ## 1. all
     ##   返回符合条件的所有数据，可以通过下标获取相应的对象
     # 3.  ## 结果： QuerySet
     # user = User.objects.all()
     # print(user)
     # print(user[11].user_name)
     # print(user[11].age)
     # return HttpResponse("查询数据")

    # for one in user:
  # print (one)
    # print(one.user_name)
    return HttpResponse("查询数据")



    # filter(条件)  返回为queryset  可通过下标或者循环获取对象的信息
def getuser(request):
    # user=User.objects.filter(age=22)
#     print(user)
#     print(user[0].age,user[0].user_name)


    # exclude(条件)  只是返回不符合条件的对象
    # shuju=User.objects.exclude(age=29)
    # print(shuju)


    # first()返回值为只是符合条件的第一个对象
    # user=User.objects.filter(age=20).first()
    # print(user)
    # last() 返回值只是符合条件的最后一个对象
    # user=User.objects.filter(age=20).last()
    # print(user)

    # user=User.objects.filter(age=20).all()
    # print(user)

# order_by ()排序  写条件  第一种排序方式
#     user=User.objects.filter(age=20).order_by("id","age").first()
#     print(user)
#
#     user = User.objects.filter(age=20).order_by("-id").first()
#     print(user)

    # reverse()反转 返回结果为Queryset() 3.
    ## reverse 使用条件，reverse 之前的结果必须是排序的，
    # 可以使用order_by或者ordering，先进行排序
    # user=User.objects.order_by("id").reverse()
    # print(user)
    # print("*"*11)
    # user=User.objects.all()
    # print(user)

    # values() 返回值是Queryset  列表  中间有个字典 不同的是字典形式返回的
    # 返回的是queryset ，比较特殊，得到的是[{}, {}] select * from user;
    # user=User.objects.values()
    # print(user)
    # print(user[0]["user_name"])#select user_name,age from user;

# count() 计数
#     user = User.objects.values("user_name", "age").count()
#     print(user)
#     user = User.objects.filter(id=11).values("user_name", "age")
#     print(user)


      ## count   计数
  ## 返回 数字

    # num = User.objects.filter(age=20).count()
    # print(num)
    # num = User.objects.count()
    # print(num)


    ##   exists 判断数据是否存在
  ## 返回值为  布尔值  True 和 False
    # flag = User.objects.filter(age=20).exists()
    # print(flag)

    ## 切片
     ##类似于  sql 中 limit 对象为Queryset类型的时候才可以使用切片
    # user = User.objects.all()[0:2]
    # print(user)

    # QuerySet：查询集，表示从数据库中查到数据的集合
    # 特性：
    # 惰性：创建好的查询集
    # 不会直接访问数据库，不会直接和数据库进行交互，当被调用的时候，才会访问数据库

    return HttpResponse("filter条件查询获取对象")



def update_user(request):
    # update和save都可以完成更新数据的操作，但是用的地方不一样
    # update是属于queryset的方法
    # queryset.update(属性=value)
    # save
    # 是属于对象的方法
    # 获取到对象，对象.save()

    # user=User.objects.get(id=2)
    # user.user_name="php"
    # user.save()
    #
    # user=User.objects.filter(id=3).first()
    # user.user_name="c++"
    # user.save()

# 调用save()方法前边是一个对象   对象的方法
#     user=User.objects.filter(age=21).all()
#     for one in user:
#         one.user_name="python"
#         one.save()

    # User.objects.filter(id=25).update(user_name="软件测试")
    # User.objects.get(id=24).update(user_name="java")不可用
    return HttpResponse("更新以及修改数据")


def delete_user(request):
    # user = User.objects.filter(age=22).delete()
    # print(user)
    # User.objects.filter(age=20).delete()#Queryset 类型
    return HttpResponse("删除元素")


def doubleline(request):



## 双下划线查询
	## __lt   小于
##  查询  id 小于10 的数据
	# data = User.objects.filter(id__lt=10).all()
# print(data)
	## __gt   大于
	## 查询 id 大于 10 的数据
	# data = User.objects.filter(id__gt =10).all()
	# print(data)
	## __lte  小于等于
	# id 小于等于10 的数据
	# data = User.objects.filter(id__lte =10).all()
	# print(data)
	## 报错  不能直接使用 大于 小于号
	# data = User.objects.filter(id < 10).all()
	# print(data)
	## __gte  大于等于

	## __in  范围查询
	## 查询 id 为 8 9 10 99 100
	# data = User.objects.filter(id__in = [8,9,10,99,100]).all()
	# print(data)
	# data = User.objects.exclude(id__in = [8,9]).all()
	# print(data)

	## __contains 模糊查询
    # data = User.objects.filter(user_name__contains="p").all()
	# print(data)
	# data = User.objects.filter(user_name__contains="lao").all()
	# print(data)
	# data = User.objects.filter(user_name__contains="ao").all()
	# print(data)
	## __icontains 忽略大小写的模糊查询
	# data = User.objects.filter(user_name__icontains="lao").all()
	# print(data)

	##  __startswith  开头
    # data = User.objects.filter(user_name__startswith="lao").all()
    # print (data)
## __istartswith 忽略大小写
	# data = User.objects.filter(user_name__istartswith="lao").all()
	# print (data)
	## __endswith 判断结尾
	#  __iendswith 判断结尾 忽略大小写
	# data = User.objects.filter(user_name__endswith='qi').all()
    # print(data)
    return  HttpResponse("双下划线")



def add_f(request):
    # 一对多 第一种增加数据的方式   create()方法
    # Publish.objects.create(name="上海出版社",address="上海")
    # Publish.objects.create(name="河北出版社", address="河北")
    # Publish.objects.create(name="吉林出版社", address="吉林")
    # Book.objects.create(name="背影",pub_id=1)
    # Book.objects.create(name="故事与她", pub_id=3)
    # Book.objects.create(name="青莲剑歌", pub_id=6)
    # Book.objects.create(name="二天一流", pub_id=6)
    # Book.objects.create(name="如意金箍", pub_id=7)
    # Book.objects.create(name="东游记", pub_id=7)
    # 第二种
      ## 正向 从外键所在的表到关联表
    # publish_obj = Publish.objects.filter(name="上海出版社").first()
    # Book.objects.create(name="python全栈", pub=publish_obj)

     ## 反向 从关联表到外键所在的表
   ## 拿到 publish的对象

    # publish_obj = Publish.objects.filter(name="河北出版社").first()
    #
    # publish_obj.book_set.create(name="python 爬虫")

    return  HttpResponse("一对多关系增加操作")

def get_f(request):
   ## 进行一对多关系的查询
      ## 查询河北出版社的书
      # publish_obj = Publish.objects.filter(name="河北出版社").first()
      # book_obj = Book.objects.filter(pub_id= publish_obj.id).all()
      # print(book_obj)

      ## 查询 老人与海 属于哪个出版社、
      # book_obj = Book.objects.filter(name="老人与海").first()
      # pub_obj = Publish.objects.filter(id=book_obj.pub_id).first()
      # print(pub_obj.name)

   ## 正向  从外键所在的表到关联表
     # 查询 python爬虫 属于哪个出版社、
     # book_obj = Book.objects.filter(name="python 爬虫").first()
     # publish_obj = book_obj.pub
     # print(publish_obj)
     # print(publish_obj.name)
  ## 反向  从关联表到外键所在的表
     # 查询上海出版社的书
     # publish_obj = Publish.objects.filter(name="上海出版社").first()
     # book_obj = publish_obj.book_set.values("name")
     # print(book_obj)

     return HttpResponse("一对多关系查询")


def update_f(request):

     ## 一对多关系的修改
      ## update   update    set
      ## 使用 obj.id

    return  HttpResponse("更新和修改关系哦")




def delete_f(request):




    return HttpResponse("删除")


def about(request):
    id = 1
    article = Article.objects.get(id=id)
    return render_to_response("about.html",locals())

def index(request):
    article=Article.objects.order_by("-date")[:6]
    one = article[0]
    print(one.author)
    print(one.type.first())

    recommend_article=Article.objects.filter(recommend=1).order_by("-date")[7]
    # click.article=Article.objects.order_by("-click")[:12]

    return render_to_response("index.html",locals())

def listpic(request):
    return render_to_response("listpic.html")

def newslistpic(request,page):
    # article=Article.objects.all().order_by("id")
    # pagnitor_obj=Paginator(article,5)
    # page_obj=pagnitor_obj.page(page)
    #
    # page_num=page_obj.number
    #
    # start = page_num-2
    # if start <= 2:
    #    start=1
    #    end =start +5
    # else:
    #    end =page_num+3
    #    if end >=pagnitor_obj.num_pages:
    #        end=pagnitor_obj.num_pages +1
    #        start = end -5
    # page_range=range(start,end)

    return render_to_response("newslistpic.html",locals())

def article_p(request):

    return  HttpResponse("article.html")

def choices_test(request):
    # data=Author.objects.get(id=3)
    # gender=data.gender
    # print(gender)
    # gender=data.get_gender_display()
    return HttpResponse("choices_test")


def add_article(request):
    # for i in range(10):
    #     article=Article()
    #     article.title="title_%s" % i
    #     article.content="content_%s" % i
    #     article.description="description_%s" % i
    #     article.author=Author.objects.get(id=1)
    #     article.save()
    #
    #     article.type.add(Type.objects.get(id=1) )
    #     article.save()
        return HttpResponse("article add")



def fy_test(request,page):
    print(page)


    ## 查询文章的方法
    # article = Article.objects.all().order_by("id")
    # print(article)
    ## Paginator(数据集，每页展示的条数)
    # paginator_obj = Paginator(article,10)
    # print(paginator_obj)
    # print(paginator_obj.count)    ### 数据的总条数
    # print(paginator_obj.num_pages)   ###  总页数
    # print(paginator_obj.page_range)   ##  range(1, 4)

    # page_obj = paginator_obj.page(page)
    # print(page_obj)   #   <Page 1 of 11>
    ## 循环遍历  得到分页之后的数据
    # for one in page_obj:
    #     print(one)
    # print(page_obj.has_next())    ## 是否有下一页  True  False
    # print(page_obj.has_previous())    ## 是否有上一页  True  False
    # print(page_obj.number)    ## 返回当前所在的页码
    # print(page_obj.previous_page_number())   ## 上一页的页码
    # print(page_obj.next_page_number())     ## 下一页的页码
    # print(page_obj.has_other_pages())   ## 是否有其他的页

    return HttpResponse("fy test")


def indexxx(request):

    return render(request,"indexxx.html")


# FILES     传的文件例如： 图片，文档
# GET      get请求传递的参数
# POST     post请求传递的参数
# method  获取到请求的方式  GET POST
# scheme  请求的协议   http  https
# path    请求的路径
# META   请求的信息
# META.OS  请求的系统
# META.HTTP_REFERER  请求的来源
# META.HTTP_HOST   请求的主机 + port
# form 定义一个表单域  双标签
# action    请求的地址，默认当前的路径
# method   请求的方式   get   post
#
# input
# id       用来和js在一起使用
# class     css 一起使用
# name    用来传递到后端数据的key
# value    默认值
# type		类型
# text  文本
# password  密码
# select 下拉框
# option  选项
# textarea   文本框
# radio  单选框
# checkbox  多选框
#
# 提交的按钮
# submit
# button
# 提交按钮     点击将form表单的内容提交到后端
# 单纯的按钮   常用来触发  js 的方法




# get请求传参
# def get_test(request):
#     data = request.GET
# 	print(data)
# 	name = request.GET.get("name")
# 	age = request.GET.get("age")
#     return HttpResponse("get_test，姓名为{}，年龄为{}".format(name,age))



# post请求传参


#
# def post_test(request):
# 	data = request.POST
# 	print(data)
# 	name = request.POST.get("name")
# 	age = request.POST.get("age")
# 	return HttpResponse("posttest 姓名{} 年龄{}".format(name,age))




# 使用form表单完成get请求
# 1、创建html文件，编写form表单
# 2、编写视图，路由，返回页面
# 3、页面中填写数据，并进行提交
# 4、视图中获取到了数据，进行业务的处理，并返回
#
# 需求：  通过输入文章的标题，返回包含输入内容的文章标题
# def getdemo(request):
# 2.	    # getdemo 视图完成功能
# 3.	        ## 1.  提供form表单页面
# 4.	        ## 2. 获取用户表单中输入的数据，进行处理，并返回结果
# 	data = request.GET
# 	print(data)
# 	search = request.GET.get("search")
# 	print(search)
# 	data = request.GET.getlist("search")
# 	print(data)
# 11.
# 12.	    ## 接收请求  处理请求   返回响应
# 13.	    ## 获取到关键字
# 14.	    search = request.GET.get("search")
# 15.	    ## 查询数据库  得到文章的标题
# 16.	    if search:
# 17.	        ## 查询数据库
# 18.	        article = Article.objects.filter(title__contains=search).values("title")
# 19.	        if len(article) == 0:
# 20.	            article = "没有对应的文章"
# 21.	    ## 返回结果
# 22.
# 23.	    return render_to_response("getdemo.html",locals())
# 1.	<!DOCTYPE html>
# 2.	<html lang="en">
# 3.	<head>
# 4.	    <meta charset="UTF-8">
# 5.	    <title>get form demo</title>
# 6.	</head>
# 7.	<body>
# 8.
# 9.	<form action="">
# 10.
# 11.	    搜索：<input type="text" name="search">
# 12.	    <input type="submit" value="搜索">
# 13.	</form>
# 14.	    <p>
# 15.	        {{ article }}
# 16.	    </p>
# 17.
# 18.	</body>
# 19.	</html>

# 1.	class User(models.Model):
# 2.	    username = models.CharField(max_length=32,verbose_name="用户名")
# 3.	    password = models.CharField(max_length=32,verbose_name="密码")
# 4.	    create_time = models.DateTimeField(auto_now=True,verbose_name="创建时间")
# 5.	    class Meta:
# 6.	        db_table="user"



def setPassword(password):
    ### 需要实例化  md5 对象
    md5 = hashlib.md5()
    ## 对password 进行加密  参数为 bytes 类型
    md5.update(password.encode())
    result = md5.hexdigest()  ## 得到一个 16进制的加密结果
    return result

def ajaxdemo(request):
    return render(request,"ajaxdemo.html")


def ajax_get_req(request):
    """
      处理ajax 的get请求
          获取到ajax的值，进行查询数据库库，判断用户是否存在
      :param request:
          username  用户的账号
      :return:
          返回是否存在的结果
      """
#     username = request.GET.get("username")
#     print(username)
#     result = {"code":10000,"msg":""}
#     if username:
#         flag = User.objects.filter(username = username).exists()
#         if flag:
#             ## True  账号存在
#             result = {"code": 10001, "msg": "账号存在，请换一个"}
#         else:
#             ## flase  账号不存在
#             # message = "账号不存在"
#             result = {"code": 10000, "msg": "账号不存在,可用"}
#     else:
#         # message = "账号不能为空"
#         result = {"code": 10002, "msg": "账号不能为空"}
#     # return HttpResponse(message)
#     return JsonResponse(result)
#
# def ajax_post_req(request):
#     """
#     完成注册的需求
#     :param request:
#         username
#         password
#             将数据写入数据库中
#     :return:
#         Json对象  成功或者失败
#     """
#
#     result = {"code":10000,"msg":""}
#     username = request.POST.get("username")
#     password = request.POST.get("password")
#     # print(request.POST)
#     if username and password:
#         ## 保存数据
#         try:
#             User.objects.create(username=username,password=setPassword(password))
#             result = {"code": 10000, "msg": "注册成功"}
#         except:
#             result = {"code":10002,"msg":"注册失败"}
#     else:
#         result = {"code": 10001, "msg": "请求参数为空"}
#     return JsonResponse(result)


#
from .forms import UserForm
# def register(request):
    # 处理了 get请求，返回了注册页面
    ## 接收到用户的注册请求   post请求
    ## 将用户的数据   保存到数据库中
    ## 判断请求的方式
    # userform = UserForm()
    # if request.method == "POST":
        # data = request.POST
        # print(data)
        # username = request.POST.get("username")
        # password = request.POST.get("passwd")
        # data = UserForm(request.POST)
        # if data.is_valid():
            ## 进行校验，成功之后 返回 True  失败返回 Flase
            ##  获取到校验成功的数据
    #         print(data.cleaned_data)
    #         username = data.cleaned_data.get("username")
    #         password = data.cleaned_data.get("password")
    #         flag = User.objects.filter(username=username).exists()
    #         if flag:
    #             message = "用户已经存在"
    #         else:
    #             User.objects.create(username=username,password=setPassword(password))
    #             message = "注册成功"
    #     else:
    #         ## 校验失败
    #         message = data.errors
    # return render(request,"register.html",locals())
    #



def set_cookie(request):

  return HttpResponse("设置cookie")
  # 将来要返回的对象用一个变量来接收
 #     response = HttpResponse("设置cookie")
 #     response=render(request,"listpic.html")

   ## 设置cookie
   ## 1、 如果需要设置多个cookie 再写一行进行设置
   ## 2、cookie中不要使用中文
     # response.set_cookie("username","laoliu")
     # response.set_cookie("age",27)
     # return response
     # return HttpResponse("设置cookie")  没用


def get_cookie(request):
#     data = request.COOKIES
#     username = request.COOKIES.get("username")
#     age = request.COOKIES.get("age")
#     print(username)
#     print(age)
      return HttpResponse("获取cookie")

from django .http import HttpResponseRedirect


def delete_cookie(request):
    ## 删除cookie
    response = HttpResponse("删除cookie")
   ## 参数为  要删除cookie的key
    # response.delete_cookie("username")
    # response.delete_cookie("age")
    # return response


def set_session(request):
    request.session["username"]="didi"
    return HttpResponse("设置session")
    # return request
def get_session(request):
    username=request.session.get("username")
    return HttpResponse(username)

def delete_session(request):
    username = request.session.get("username")
    print(username)
    del request.session["username"]
    return HttpResponse("删除session")

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username and password:
            user = User.objects.filter(username=username, password=setPassword(password)).first()
            if user:
                response = HttpResponseRedirect("/")
                # response = HttpResponse("登录成功")
                response.set_cookie("username", user.username)
                # response.set_cookie("user_id", user.id)
                request.session["username"] = user.username
                return response
            else:
                return HttpResponse("账号密码不正确")
        else:
            return HttpResponse("账号密码 不能为空")
    return render(request,"login.html")



def rase_vue(request):
    return render(request,"rase_vue.html",locals())
