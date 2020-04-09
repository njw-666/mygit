# import logging
#
# ## 进行日志的配置   日志的等级
# logging.basicConfig(level=logging.DEBUG)
# """
# level 要收集的日志等级    默认是 warning
# """
# logging.debug("我是debug")
# logging.info("我是info")
# logging.warning("我是warning")
# logging.error("我是error")
# logging.critical("我是crticle")
# # 可以设置日志等级，将日志打印到控制台
# #
# # 可以通过参数，设置日志的格式，以及日志的输出位置（日志文件，控制台）
#
#
# import logging
#
# ## 进行日志的配置   日志的等级
# ## 控制日志输出的格式
# format = "%(asctime)s 【%(levelname)s】 %(message)s"
# #  %(asctime)s 时间
# #  %(levelname)s  日志的级别
# #  %(message)s 日志的信息内容
# datefmt = "%Y-%m-%d %H:%M:%S"
# ##收集日志   将日志写入文件中
# file_handlers = logging.FileHandler("test.log",encoding="utf-8")
# ## 控制台输出日志
# stream_handlers = logging.StreamHandler()
#
# logging.basicConfig(level=logging.DEBUG,format=format,datefmt=datefmt,handlers=[file_handlers,stream_handlers])
# """
# level 要收集的日志等级    默认是 warning
# format  可以定义输出的日志的格式
# datefmt   时间格式
# handlers   句柄  文件句柄
# """
# logging.debug("我是debug")
# logging.info("我是info")
# logging.warning("我是warning")
# logging.error("我是error")
# logging.critical("我是crticle")












import logging
format="%(asctime)s 【%(levelname)s】 %(message)s"
datefmt="%Y-%m-%d $H:%M:%S"
file_handlers=logging.FileHandler("text.log",encoding="utf-8")
stream_handlers=logging.StreamHandler()

logging.basicConfig(level=logging.DEBUG,format=format,datefmt=datefmt,handlers=[file_handlers,stream_handlers])
logging.debug("1")
logging.info("2")
logging.warning("3")
logging.critical("4")
logging.error("5")
