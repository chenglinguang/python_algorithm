#!/usr/bin/env python3 

#-*- coding:utf-8 -*-

import smtplib 

server=smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login('','')
server.sendmail('','@tmomail.net','Hello!')




