from main import db
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
class Label(Model):
    name=db.Column(db.String(32))  #标签名
    description=db.Column(db.Text)   #标签描述
    course=db.relationship("Course",backref="label")
class Course(Model):
    # id  = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(32))
    description = db.Column(db.String(128))   ## 课程描述
    picture=db.Column(db.String(64))
    show_number=db.Column(db.Integer)
    status=db.Column(db.Integer,default=1)
    type=db.Column(db.Integer,default=1)
    time_number=db.Column(db.Integer)
    label_id = db.Column(db.Integer, db.ForeignKey("label.id"))

    # def addcourse(self):
    #     self.name="good" + self.name
    #     # db.session.add(self.name)
    #     # db.session.commit()
    #     self.save()

db.create_all()