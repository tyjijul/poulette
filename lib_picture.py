#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' LIB TO TAKE PICTURE '''
from subprocess import call
import time, platform, glob, os 
from PIL import Image
import glob, os
SYSTEM = platform.system()
PATH = "static/img/"

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

fromaddr = "YOUR EMAIL"
toaddr = "EMAIL ADDRESS YOU SEND TO"

msg = MIMEMultipart()

def take_pic():
    ''' declenchement direct '''
    filename = "IMG_Poulette_"+time.strftime("%Y-%m-%d_%H-%M-%S_")+".jpg"
    fullpath = PATH+filename
    if SYSTEM == 'Darwin':
        call(["imagesnap", "-w", "1", str(fullpath)])
    else :
        call(["raspistill", "-n", "-o", fullpath])
    thumbnail(filename)
    return 1

def thumbnail(name_img):
    im = Image.open(PATH+name_img)
    im.thumbnail((128, 128), Image.ANTIALIAS)
    if name_img[0:2] != "T_":
        # prefix thumbnail file with T_
        im.save("static/thumbnail/T_" + name_img, "JPEG")


def send_mail_pic(path):
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "Photo send from Poulette Life System !"
	body = "Hello c'est poulette ! voici la photo"
	msg.attach(MIMEText(body, 'plain'))
	filename = "00011_photo.jpg"
	attachment = open(path, "rb")
	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
	msg.attach(part) 
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "superpoulette")
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()

def del_pic(path):
	parsePath = path.split("/")
	os.remove("static/img/"+parsePath[2])
	os.remove("static/thumbnail/"+parsePath[2])


def sendEmail():	
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "SUBJECT OF THE EMAIL"
	
	body = "TEXT YOU WANT TO SEND"
	
	msg.attach(MIMEText(body, 'plain'))
	
	filename = "NAME OF THE FILE WITH ITS EXTENSION"
	attachment = open("PATH OF THE FILE", "rb")
	
	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
	
	msg.attach(part)
	
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "YOUR PASSWORD")
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()

if __name__ == '__main__':
	#take_pic()

