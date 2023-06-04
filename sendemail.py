import smtplib
from email.mime.text import MIMEText 
from email.utils import formataddr
import os

class sendemail:
    def __init__(self,toemail):
        self.toEmail = toemail #接收者邮箱
    
    def sent_email(self,bookdate,booktime):
        host_server = 'smtp.qq.com'
        port = 465  
        sender = '353227876@qq.com'##发送者的qq号  
        senderalias  =  'Badminton <353227876@qq.com>' 
        password = '' #QQ邮箱密码
        receiver = self.toEmail  
        body = '<h1>[预定提醒]：</h1><p>已成功预定。日期：'+ bookdate +'，时间段：'+ booktime +'。</p>' #要发送的文本
        msg = MIMEText(body,'html') 
        
        msg['subject'] = '羽毛球预定提醒' #邮件主题 
        msg['from'] = senderalias
        msg['to'] = receiver
        s = smtplib.SMTP_SSL(host_server)
        s.login(sender,password) 
        s.sendmail(sender,receiver,msg.as_string()) 
        s.quit()