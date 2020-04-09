#项目的初始化文件
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import CSRFProtect  #csrf保护
db=SQLAlchemy()
migrate=Migrate()
csrf=CSRFProtect()  #实例化
def createApp(obj):
    # 实例化app
    app = Flask(__name__)
    app.config.from_object(obj)
    db.init_app(app)  #惰性加载
    migrate.init_app(app,db)
    csrf.init_app(app)
    from blueprint.course import course_bl
    from blueprint.user import user_bl
    # 将申明好的蓝图注册进来
    app.register_blueprint(course_bl, url_prefix="/course")
    app.register_blueprint(user_bl, url_prefix="/user")
    #使用装饰器，注册一个要被执行的方法，请求钩子
    @app.before_first_request
    def first_request():
        print("before_first_request")
    @app.before_request
    def req():
        print(" before_request")
    # @app.after_request
    # def afger_req(response):
    #     print("after_request")
    # @app.teardown_request
    # def teardown_req(response):
    #     print("teardown_request")
    #     return response

    return app



