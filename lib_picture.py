#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' LIB TO TAKE PICTURE '''
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
from subprocess import call
import time, platform, glob, os 
SYSTEM = platform.system()
fromaddr = "poulettemylove@gmail.com"
toaddr = "julien.cav@gmail.com"
msg = MIMEMultipart()

PATH = "static/img/"

def take_pic():
    ''' declenchement direct '''
    filename = "IMG_Poulette_"+time.strftime("%Y-%m-%d_%H-%M-%S_")+".jpg"
    fullpath = PATH+filename
    if SYSTEM == 'Darwin':
        call(["imagesnap", "-w", "1", str(fullpath)])
    else :
        call(["raspistill", "-n", "-o", fullpath])
    return 1




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
	#filelist = glob.glob(os.path.join(path)
    #for f in filelist:
    os.remove(path)

if __name__ == '__main__':
    RES = send_mail_pic("static/img/00011_photo.jpg")
    print(RES)


