#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' LIB TO TAKE PICTURE '''

import sys
sys.path.append('../')

import time, platform, glob, os, smtplib
from subprocess import call
from PIL import Image
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

SYSTEM = platform.system()
PATH = "static/img/"
fromaddr = "poulettemylove@gmail.com"
psswrd = "superpoulette"
msg = MIMEMultipart()

def take_pic():
    ''' declenchement direct '''
    filename = "IMG_Poulette_"+time.strftime("%Y-%m-%d_%H-%M-%S_")+".jpg"
    fullpath = PATH+filename
    if SYSTEM == 'Darwin':
        call(["imagesnap", "-w", "1", str(fullpath)])
    else :
        call(["raspistill","-t","1","-n", "-o", fullpath])
    thumbnail(filename)
    return 1

def thumbnail(name_img):
    im = Image.open(PATH+name_img)
    im.thumbnail((128, 128), Image.ANTIALIAS)
    if name_img[0:2] != "T_":
        im.save("static/thumbnail/T_" + name_img, "JPEG")


def del_pic(path):
	parsePath = path.split("/")
	os.remove("static/img/"+parsePath[2])
	os.remove("static/thumbnail/"+parsePath[2])


def sendEmail(path, email, name = "ton camion"):	
	msg['From'] = fromaddr
	msg['To'] = email.strip()
	msg['Subject'] = "Photo send from PLS !"
	
	body = "Hello c'est "+name+" ! voici la photo"
	
	msg.attach(MIMEText(body, 'plain'))
	parsePath = path.split("/")
	filename = parsePath[2]
	attachment = open(path, "rb")
	
	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
	
	msg.attach(part)
	
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, psswrd)
	text = msg.as_string()
	server.sendmail(fromaddr, email, text)
	server.quit()

if __name__ == '__main__':
	sendEmail("static/img/00028_photo.jpg", "julien.cav@gmail.com", "Simone")

