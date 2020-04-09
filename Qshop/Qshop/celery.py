# 第四步
#管理控制celery
import os
from celery import Celery
from django.conf import settings
#设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE','CeleryTask.settings')
#实例化celery 参数为celery应用的名字
app=Celery("Qshop_celery")

#加载celery设置
app.config_from_object('django.conf：settings')

#如果创建了tasks文件 就会在App中自动寻找tasks 文件
app.autodiscover_tasks(lambda :settings.INSTALLED_APPS)
