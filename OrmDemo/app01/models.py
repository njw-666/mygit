from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)  #主键
    name =models.CharField(max_length=32)  #字符串
    age = models.IntegerField()   #int 整形