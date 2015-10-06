#-*-coding:utf-8 -*-
import smtplib
import json
from email.mime.text import MIMEText

def send_mail(msg_text,subject):
	f = open('./Send_Mail/config.json')
	parameters = json.load(f)
	_user = parameters["user"]
	_pwd = parameters["pwd"]
	_to = parameters["to"]
	_stmp = parameters["stmp"]

	msg = MIMEText(msg_text)
	msg["Subject"] = subject
	msg["From"] = _user
	msg["To"]   = _to

	s = smtplib.SMTP(_stmp,timeout=60)
	s.login(_user,_pwd)
	s.sendmail(_user,_to,msg.as_string())
	s.close()

