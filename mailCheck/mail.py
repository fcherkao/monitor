#!/usr/bin/env pyhton
#-*- coding: utf-8 -*-

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

msg = MIMEMultipart()
msg['From'] = 'icinga.smtp.alert@gmail.com'
msg['TO'] = 'icinga.smtp.mail@gmail.com'
msg['SUbject'] = 'Just smth'
message = 'Bonjour'

print msg['From']
msg.attach(MIMEText(message))

mailserver = smtplib.SMTP('smtp.gmail.com',587)
mailserver.ehlo()
mailserver.starttls()
mailserver.ehlo()
mailserver.login(msg['From'],'AZqswx1234')
mailserver.sendmail(msg['From'],msg['To'],msg.as_string())
mailserver.quit()

