#!/usr/bin/env python
# -*- codeing: utf-8 -*-
"""
sendmail program

by YCom
"""
import sys
import smtplib
import datetime
from email.mime.text import MIMEText

mailto_list=["admin@xx.com"]
from_addr = "scan@xx.com"

mail_server = ""
mail_user = ""
mail_pass = ""
mail_post_fix = "xx.com"

def make_beauty(line):
    new_line =  ""
    if line[0] == '-':
        new_line = '<p style="color:red;">{0}</p>'.format(line)
    if line[0] == '+':
        new_line = '<p style="color:green;">{0}</p>'.format(line)
    else:
        new_line = '<strong>{0}</strong>'.format(line)
    return new_line

def send_mail(fromaddr,mailto,filename):
    content = []
    new_content = []
    with open(filename) as f:
        content = f.readlines()
    for line in content:
        new_content.append(make_beauty(line))

    body = ""
    for a in content:
        body = body + a

    body = "{0}".format(body)
    me = mail_user+"<"+mail_user+"@"+mail_post_fix+">"
    #msg = MIMEText(body,'html','utf-8')
    msg = MIMEText(body)
    print("Constructing msg..")
    msg['Subject'] = "scan result of "+str(datetime.date.today())
    msg['From'] = from_addr
    msg['To'] = ";".join(mailto_list)
    s = smtplib.SMTP_SSL()
    s.connect(mail_server)
    s.login(from_addr,mail_pass)
    print("connect ok.start sending..") 
    s.sendmail(from_addr,mailto_list,msg.as_string())
    s.close()
    print("success!")

if __name__ == '__main__':
    if len(sys.argv)==2:
        name = sys.argv[1]
        send_mail(from_addr,mailto_list,name)
