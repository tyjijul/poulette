#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' LIB TO TAKE PICTURE '''

from email import encoders
from subprocess import call
import time, platform, glob, os 
SYSTEM = platform.system()

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
	print("IMPOSSIBLE IN MAC OS")

def del_pic(path):
	#filelist = glob.glob(os.path.join(path)
    #for f in filelist:
    os.remove(path)





