from flask_wtf import FlaskForm
import wtforms
from wtforms import validators
def zidingyi(form,field):
    print(field.data)
    data_list=["admin","xxxx"]
    for one in data_list:
        if one in field.data:
            raise ValueError("账号中不能存在敏感字")
class UserForm(FlaskForm):
    ## 对填写的数据进行校验
    name = wtforms.StringField(
        label="账号",
        ## 校验规则
        validators = [
            validators.DataRequired(message="内容不能为空"),                 ### 必填
            validators.Email(message="必须是邮箱")  ,#### 必须是邮箱格式
            zidingyi
        ]
    )
    password = wtforms.PasswordField(
        label="密码",
        validators = [
            validators.NumberRange(message="内容必须为数字"),           #### 必须为数字
            validators.Length(min=6,max=8,message="密码为6到8位"),      ###数据的长度
            validators.EqualTo("repassword",message="密码不一致")       ### 和那个字段的内容相等
        ]
    )
    repassword = wtforms.PasswordField(label="密码")

#StringField 类似于input中的text
#PasswordField类似于input中的password
#SelectField类似于input中的select
#HiddenField类似于input中的hidden
#RadioField类似于input 中的radio



