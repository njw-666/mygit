from django.db import models
from ckeditor.fields import RichTextField
# from django.contrib.auth.models import User
## RichTextField   底层是 TextField  只是修改前端的样式，能够将输入的内容以html的格式进行重新排版
# Create your models here.+
from ckeditor_uploader.fields import RichTextUploadingField     ### 支持文件上传
class User(models.Model):
    id = models.AutoField(primary_key=True)  #主键
    user_name =models.CharField(max_length=32,verbose_name="用户名")  #字符串
    age = models.IntegerField(verbose_name="年龄")   #int 整形
    phone = models.CharField(max_length=11,verbose_name="手机号码")
    email = models.EmailField(default="11111@qq.com",verbose_name="电子邮箱")

    #def __str__(self):#重写字符串的返回类型
     #   return self.user_name

    class Meta:
        db_table="user" #修改表的名字
        # 排序的第二种方式和写法
        # ording=["-id","age"]
        verbose_name_plural="用户"#去掉站点显示的s

class Subject(models.Model ):
    name = models.CharField(max_length=32,verbose_name="学科的名字")
    start_time=models.DateField(verbose_name="开始时间")
    class Meta:
        db_table = "subject"#修改表的名字
        verbose_name="学科" #修改站点显示的表名为中文  对表进行备注
        verbose_name_plural="学科" #修改站点显示的表的后缀s 去掉复数的形式


class Publish(models.Model):
    # id =1
    name=models.CharField(max_length=32,verbose_name="出版社名字")
    address = models.CharField(max_length=32,verbose_name="出版社地址")
    class Meta:
        db_table="publish"
        # verbose_name = "学科"  # 修改站点显示的表名为中文  对表进行备注
        verbose_name_plural = "publish"  # 修改站点显示的表的后缀s 去掉复数的形式


class Book(models.Model):
    name=models.CharField(max_length=32,verbose_name="书名")
    pub=models.ForeignKey(to=Publish,to_field="id",on_delete=models.CASCADE)
    # pub_id=1
    class Meta:
        db_table="book"
 #        verbose_name = "book"  # 修改站点显示的表名为中文  对表进行备注
        verbose_name_plural = "book"  # 修改站点显示的表的后缀s 去掉复数的形式
 # ## to 代表 和那个表产生关联      ## to_field 代表和关联表中的那个字段进行关联，可以不填，不填默认使用关联表的id
 #    # on_delete  代表当关联表（publish）中的数据被删除的时候，Book表要做什么行为
    # models.CASCADE 默认删除，当关联表中数据删除之后，要删除      # models.PROTECT 保护的

# choices()的用法
GENDER_STATUS =(
    (0,"女"),
    (1,"男")
)
class Author(models.Model):
    # id = models.IntegerField(primary_key=True,verbose_name="主键")
    name = models.CharField(max_length=32, verbose_name="作者姓名")
    # gender = models.CharField(max_length= 32,verbose_name="性别")  ### 1 代表 男， 0代表 女
    gender=models.IntegerField(choices=GENDER_STATUS,verbose_name="性别")
    age = models.IntegerField(verbose_name="年龄")
    email = models.EmailField(max_length= 32, verbose_name="邮箱")
    def __str__(self):
        return self.name

    class Meta:
        db_table="author"
        # verbose_name_plural ="author"


class Type(models.Model ):
    # id = models.AutoField(primary_key=True, verbose_name="主键")
    name = models.CharField(max_length=32,verbose_name="类型名字")
    description=models.TextField(verbose_name="描述")
    def __str__(self):
        return self.name
    class Meta:
        db_table="type"
        # verbose_name_plural ="type"


class Article(models.Model):
    # id = models.AutoField(primary_key=True, verbose_name="主键")
    title = models.CharField(max_length=32, verbose_name="标题")
    date = models.DateField(auto_now=True ,verbose_name="创建时间")
    # content = models.TextField(verbose_name="文章内容")
    # description = models.TextField(verbose_name="文章描述")
    # content = RichTextField(verbose_name="内容")
    content = RichTextUploadingField(verbose_name="内容")
    description = RichTextField(verbose_name="描述")
    author = models.ForeignKey(to=Author, to_field="id", on_delete=models.CASCADE)
    picture=models.ImageField(upload_to="images",verbose_name="图片",default="22.jpg")
    recommend=models.IntegerField(default=0,verbose_name="点击率")
    # 当使用模型中
    # ImageField字段属性的时候， 需要依赖pillow
    # 模块，并且在settings中配置资源的位置
    type = models.ManyToManyField(to=Type)
    def __str__(self):
        return self.title
    class Meta:
       db_table = "article"




class Ser(models.Model):
    username = models.CharField(max_length=32,verbose_name="用户名")
    password = models.CharField(max_length=32,verbose_name="密码")
    create_time = models.DateTimeField(auto_now=True,verbose_name="创建时间")
    class Meta:
        db_table="ser"







