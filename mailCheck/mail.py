#!/usr/bin/env pyhton
#-*- coding: utf-8 -*-

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

msg = MIMEMultipart()
msg['From'] = 'faycal.anoar.cherkaoui@gmail.com'
msg['TO'] = 'faycal.anoar.cherkaoui@gmail.com'
msg['SUbject'] = 'Just smth'
message = 'Bonjour'


msg.attach(MIMEText(message))

mailserver = smtplib.SMTP('smtp.gmail.com',587)
mailserver.ehlo()
mailserver.starttls()
mailserver.ehlo()
mailserver.login('faycal.anoar.cherkaoui@gmail.com','Anoar-753')
mailserver.sendmail('faycal.anoar.cherkaoui@gmail.com','faycal.anoar.cherkaoui@gmail.com',msg.as_string())
mailserver.quit()

