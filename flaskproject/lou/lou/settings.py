#第一种
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/loua"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True    #1
# app.config["SQLALCHEMY_ECHO"] = True
#第二种
SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:@localhost/loua"    #2
SQLALCHEMY_TRACK_MODIFICATIONS=True
DEBUG=True

#第三种
class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/loua"  # 2
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = False

class TextConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/loua"
    DEBUG = True



