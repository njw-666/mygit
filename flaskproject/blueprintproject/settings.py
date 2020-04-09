#配置文件，对照着没啥事
import os
class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:@localhost/hello"    #2
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    # SQLALCHEMY_ECHO=True
    DEBUG=True
    STATICFILES_DIRS = os.path.join(BASE_DIR, 'static')
    SECRET_KEY = "123456"

class TextConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/hello"
    DEBUG =False

