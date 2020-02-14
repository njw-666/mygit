# 编写自定义过滤器

# 导包

from django import template
# 实例化对象
register = template.Library()


# 前端调用
# {{age | myadd }} age = num + num
# 编写过滤器方法
@register.filter(name="MyAdd")
def myadd(num):
    return num + num

@register.filter()
def my_two_add(num1,num2):
    return num1 + num2
