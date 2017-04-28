#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' LIB TO TAKE PICTURE '''
from subprocess import call
import time, platform 
SYSTEM = platform.system()

PATH = "static/img/"

def take_pic():
    ''' declenchement direct '''
    filename = "IMG_Poulette_"+time.strftime("%Y-%m-%d_%H-%M-%S_")+".jpg"
    fullpath = PATH+filename
    if SYSTEM == 'Darwin':
        call(["imagesnap", "-w", "1", str(fullpath)])
    else :
        call(["fswebcam", "-r", "640x480", fullpath])
    return 1




def send_mail_pic(path):
    #filename = "IMG_Poulette"+str(line-1)+".jpg"
    #PATH = "../gallery/"
    fullpath = path
    call(["mutt", "-s", "Poulette Picture", "-a", fullpath, "--", "julien.cav@gmail.com"])
    #call(["mutt -s 'Ma voiture' -a *.jpg -- julien.cav@gmail.com < mon_message.txt"])
    print("La photo est envoyé à l'adresse julien.cav@gmail.com")

if __name__ == '__main__':
    RES = take_pic()
    print(RES)
