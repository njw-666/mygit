from __future__ import absolute_import
from Qshop.celery import app

@app.task
def Test():
    ## 没有参数
    ## 任务
    import time
    time.sleep(20)
    print("hello world")

# 有参数的任务
@app.task
def Myprint(num):
    print(num)

from sdk.sendDD import senddingding
@app.task
def senddingd(params):
    # 发送钉钉的异步任务
    senddingding(params)



#5用于编写任务 此文件应在Qshop 主目录下新建的子应用中存在
# from __future__ import absolute_import
# from Qshop.celery import app
# @app.task
# def TaskTest():
#
#     print("hellow meizhi")