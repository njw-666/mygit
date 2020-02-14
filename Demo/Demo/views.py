import time
import datetime
from django.http import HttpResponse
from django.template import Template,Context





def index(request):
    return HttpResponse("hello world")

def about(request):
    return HttpResponse("别看了，过的比你好")

def ntime(request):
    return HttpResponse(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))

# def dtime(request):
#     return HttpResponse(datetime.datetime.ctime(datetime.datetime.now()))

def ttime(request):
   return HttpResponse (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

def retest(request,id):
    print(id)
    return HttpResponse('叫哥哥')

# 有瑕疵的视图
def testdemo(request,year,city):
    result="我%s年在%s" % (year,city)
    return HttpResponse(result)


def test(request,city,id):
    result="%s,%s" % (id,city)
    return HttpResponse(result)

def indexhtml(request):
    """
    编写一个html页面
    :param request:
    :return:
    """

    html =  """
    <html>
    <head></head>
    <body>
    <h1>我是小哥哥</h1>
    <img src="http://pic.topmeizi.com/wp-content/uploads/2017a/04/06/01.jpg" >
    姓名：{{name}}
    年龄：{{age}}
    </body>
    </html>
    
    """
    # 返回一个响应对象
    # return HttpResponse(html)
    # 渲染动态的数据
    # 1创建模板
    template_ojb = Template(html)
    # 2构建动态数据
    parmas = {"name":"xiaoze","age":30}
    content_obj=Context(parmas)
    # 3. 构建动态页面 将动态数据 渲染到静态页面上
    result = template_ojb.render(content_obj)
    return HttpResponse(result)

# 第一种方式
from django.template.loader import get_template
def getindex1(request):
    template_obj = get_template("index.html")
    parmas = {"name": "xiaocang", "age": 33}
    result = template_obj.render(parmas)
    return HttpResponse(result)

# 第二种方式
# 返回index.html页面
from django.shortcuts import render_to_response
def getindex(request):
    parmas = {"name":"xiaotiantian ","age":28}
    # render_to_response(要返回的页面),接收两个参数
    return render_to_response("index.html",parmas)

# 第三种返回的是index.html
# 	    ## 渲染的数据     name age
# 	    ## render(request,要返回的页面,动态的数据)
from django.shortcuts import render
def getindex2(request):
    parmas = {"name": "夫人", "age": 24}
    return render(request, "index.html", parmas)


def temptest(request):
    # 返回数据
    name="小星星"
    # name=""
    age=22
    # 支持列表，字典，元组，集合
    hobby = ["唱歌", "跳舞", "shopping"]
    score = {"python": 100, "java": 90, "php": 80}
    subject = ("python", "java", "php")
    # 返回数据的方式
    # 第一种
#     return render_to_response("temptest.html",
# {"name":name, "age": age, "hobby": hobby, "score": score, "subject": subject})
    # 第二种
    # parmas = {"name": "夫人", "age": 24}
    # return render(request, "index.html", parmas)
    # 第三种
    now_time = datetime.datetime.now()
    time.strftime("Y-m-d H:m:s")

    # 有瑕疵
    myjs = """
    <srcipt>
        alert("myjs"):
    </srcipt>
    """


    return render_to_response("temptest.html",locals())


def statictest(request):
    return render_to_response("statictest.html")


def index1(request):
    return render_to_response("index1.html")

def about1(request):
    return render_to_response(("about1.html"))

def listpic1(request):
    return render_to_response("listpic1.html")

def newslistpic1(request):
    return render_to_response("newslistpic1.html")

def base(request):
    return render_to_response("base.html")

def demo01(request):
    return render_to_response("demo01.html")

