import smtplib
from email.mime.text import MIMEText
subject="关于学习"
content="我爱学习，学习使我快乐,学习能有美妞相伴"
sender="1037769494@qq.com"
recver="""1041104279@qq.com"""
password="nuszicgbtjfcbbif"


message=MIMEText(content,'plain','utf-8')
message["Subject"]=subject
message["Form"]=sender
message["To"]=recver
smtp=smtplib.SMTP_SSL("smtp.qq.com",465)
smtp.login(sender,password)
smtp.sendmail(sender,recver.split(","),message.as_string())
smtp.close()
