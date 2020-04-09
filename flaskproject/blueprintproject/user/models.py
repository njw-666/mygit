from main import db
# from blueprintproject import db
class Model(db.Model):
    __abstract__=True
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    def save(self):
        db.session.add(self)
        db.session.commit()
    def update(self):
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
#多对多关系创建
user_course=db.Table(
    "user_course",
    db.Column("id",db.Integer,primary_key=True,autoincrement=True),
    db.Column("user_id",db.Integer,db.ForeignKey("user.id")),
    db.Column("course_id",db.Integer,db.ForeignKey("course.id"))
)

# class User(Model):
#     ## 模型 不会像django模型中 自动创建id 主键
#     # id = db.Column(db.Integer,primary_key=True,autoincrement=True)
#     name = db.Column(db.String(32))
#     password = db.Column(db.String(32))  ## 密码
#     role_id = db.Column(db.Integer, db.ForeignKey("role.id"))
#     role = db.relationship("Role", backref="user")
#     #backref反向的关系
#     course=db.relationship("Course",secondary=user_course,backref="user")
#
#
# class Role(Model):
#     r_name = db.Column(db.String(32))  ## 角色名字
#     description = db.Column(db.String(32))
    #,uselist=False
    # user=db.relationship("User",backref="role",uselist=False)
    ## 角色描述
    ## relationship  模型间的一种关系 ，user只是代表关系，并不会表现在数据库中
    ## User 关联模型的类名
    ## backref 反向映射
    #一对一 uselist=False
