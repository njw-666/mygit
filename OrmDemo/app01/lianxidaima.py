# 先引入模块
import hashlib
def setPassword(password):
    # 实例化对象
    md5=hashlib.md5()
    # 对password进行加密，参数为bytes类型
    md5.update(password.encode())
    result=md5.hexdigest()
    return result




from django import forms
class UserForm(forms.Form):
    username=forms.CharField(max_length=8,label="姓名",required=True)
    password=forms.CharField(max_length=8,min_length=6,label="密码")


    #   max_length 最大长度#   min_length  最小长度

    #   required  是否为空，默认为True代表不可为空#  label  标签的内容




from .forms import UserForm
def register(requset):
    userform=UserForm()
    if request.method == "POST":
        data = request.POST
        print(data)
        username=request.POST.get("username")
        password=request.POSt.get("password")
        flag=User.objects.filter(username=username).exists()



### 固定写法
    def clean_username(self):
        ## 校验数据##获取数据

        username = self.cleaned_data.get("username")
        ## 校验规则
        if username == "admin":
            ## 校验不通过
            self.add_error("username","用户名不能是admin")
        else:
            ## 校验通过
            return username




from django.db import models
from ckeditor.fields import RichTextField
## RichTextField   底层是 TextField  只是修改前端的样式，能够将输入的内容以html的格式进行重新排版
from ckeditor_uploader.fields import RichTextUploadingField     ### 支持文件上传





# Create your models here.





GENDER_STATUS = (
    (0,"女"),
    (1,"男")
)


class Author(models.Model):
    name = models.CharField(max_length=32,verbose_name="作者姓名")
    # gender = models.CharField(max_length=32,verbose_name="性别")    ### 男  女
    gender = models.IntegerField(choices=GENDER_STATUS,verbose_name="性别")    ###  1 代表  男  0 代表女
    age = models.IntegerField(null=True,blank=True,verbose_name="年龄")
    ## null = True  在数据库中 是可以为空
    ## blank = True 在表单中是可以为空

    email = models.EmailField(verbose_name="邮箱")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "author"

class Type(models.Model):
    name = models.CharField(max_length=32,verbose_name="类型名字")
    description = models.TextField(verbose_name="描述")
    def __str__(self):
        return self.name
    class Meta:
        db_table = "type"

class Article(models.Model):
    title = models.CharField(max_length=32,verbose_name="标题")
    date = models.DateField(auto_now=True,verbose_name="创建时间")
    # content = RichTextField(verbose_name="内容")
    content = RichTextUploadingField()
    description = RichTextField(verbose_name="描述")
    # content = models.TextField(verbose_name="内容")
    # description = models.TextField(verbose_name="文章描述")
    ## 由   upload_to 决定了图片上传的路径 static/images/
    ##  upload_to  当 images 目录存在的时候，直接将图片上传到iamges 目录下
    ##             当 images 目录不存在的时候，创建images目录并且完成图片的上传
    picture = models.ImageField(upload_to="images",verbose_name="图片")
    recommend = models.IntegerField(default=0,verbose_name="推荐")  ## 0 代表不推荐  1 代表推荐
    click = models.IntegerField(default=0,verbose_name="点击率")
    author = models.ForeignKey(to=Author,to_field="id",on_delete=models.CASCADE)
    type = models.ManyToManyField(to=Type)
    def __str__(self):
        return self.title
    class Meta:
        db_table = "article"



class User(models.Model):
    username = models.CharField(max_length=32,verbose_name="用户名")
    password = models.CharField(max_length=32,verbose_name="密码")
    create_time = models.DateTimeField(auto_now=True,verbose_name="创建时间")
    class Meta:
        db_table="user"






from .forms import UserForm
def register(request):
    ## 处理了 get请求，返回了注册页面## 接收到用户的注册请求   post请求
    ## 将用户的数据   保存到数据库中## 判断请求的方式
    userform = UserForm()
    if request.method == "POST":
        # data = request.POST
        # print(data)
        # username = request.POST.get("username")
        # password = request.POST.get("passwd")
        data = UserForm(request.POST)
        if data.is_valid():
            ## 进行校验，成功之后 返回 True  失败返回 Flase
            ##  获取到校验成功的数据
            print(data.cleaned_data)
            username = data.cleaned_data.get("username")
            password = data.cleaned_data.get("password")
            flag = User.objects.filter(username=username).exists()
            if flag:
                message = "用户已经存在"
            else:
                User.objects.create(username=username,password=setPassword(password))
                message = "注册成功"
        else:
            ## 校验失败
            message = data.errors
    return render(request,"register.html",locals())


from django.http import JsonResponse

## 返回  ajax 注册的页面
def ajax_register(request):
    ## 写处理业务的代码
    ## 代码  得到 数据
    return render(request,"ajax_register.html",locals())


## 处理ajax get请求
def ajax_get_req(request):
    """
    处理ajax 的get请求
        获取到ajax的值，进行查询数据库库，判断用户是否存在
    :param request:
        username  用户的账号
    :return:
        返回是否存在的结果
    """
    username = request.GET.get("username")
    print(username)
    result = {"code":10000,"msg":""}
    if username:
        flag = User.objects.filter(username = username).exists()
        if flag:
            ## True  账号存在
            result = {"code": 10001, "msg": "账号存在，请换一个"}
        else:
            ## flase  账号不存在
            # message = "账号不存在"
            result = {"code": 10000, "msg": "账号不存在,可用"}
    else:
        # message = "账号不能为空"
        result = {"code": 10002, "msg": "账号不能为空"}
    # return HttpResponse(message)
    return JsonResponse(result)



def ajax_post_req(request):
    """
    完成注册的需求
    :param request:
        username
        passwor  d
            将数据写入数据库中
    :return:
        Json对象  成功或者失败
    """

    result = {"code":10000,"msg":""}
    username = request.POST.get("username")
    password = request.POST.get("password")
    # print(request.POST)
    if username and password:
        ## 保存数据
        try:
            User.objects.create(username=username,password=setPassword(password))
            result = {"code": 10000, "msg": "注册成功"}
        except:
            result = {"code":10002,"msg":"注册失败"}
    else:
        result = {"code": 10001, "msg": "请求参数为空"}
    return JsonResponse(result)



$("#btn").click(

    function()
    {
         // console.log(1111111)
     // 获取数据
var username = $("#username").val();


var password = $("#password").val();

varurl = "http://127.0.0.1:8000/article/ajax_post_req/";
     // 构建数据字典

    var
    send_data = {

    "username": username,

    "password": password,

    "csrfmiddlewaretoken": "{{ csrf_token }}"
    	};
    	        $.ajax({
        	            url: url,
    	            type: "post",
    	            data: send_data,
    	            success :function (data) {
        	                console.log(data);
    	                $("#content").text(data["msg"]);
    	            },
    	            error :function (error) {
        	                console.log(error);
    	            }
    	        })
    	    }

