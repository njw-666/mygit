import requests
## 短信请求地址,固定不变  接口文档提供
url = "http://106.ihuyi.com/webservice/sms.php?method=Submit"
#APIID

account = "C28868327"
#APIkey
password = "b67cb2bfb579c07d1967f2eab67dbd32"
## 接收人手机号
mobile = "13472373727"
## 发送内容
content = "您的验证码是：2222。请不要把验证码泄露给其他人。"
## 请求头
headers = {
    "Content-type": "application/x-www-form-urlencoded",
    "Accept": "text/plain"
}
## 请求数据
data = {
    "account": account,
    "password": password,
    "mobile": mobile,
    "content": content,
}
## 发送请求
response = requests.post(url,headers = headers,data=data)
    #url 请求地址
    #headers 请求头
    #data 请求数据
print(response.content.decode())
