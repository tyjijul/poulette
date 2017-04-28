''' LIB TO TAKE PICTURE '''
from subprocess import call
import time, platform 

SYSTEM = platform.system()

def take_pic():
    ''' declenchement direct '''
    filename = "IMG_Poulette_"+time.strftime("%Y-%m-%d_%H-%M-%S_")+".jpg"
    path = "static/img/"
    fullpath = path+filename
    if SYSTEM == 'Darwin':
        call(["imagesnap", "-w", "1", str(fullpath)])
    else :
        call(["fswebcam", "-r", "640x480", fullpath])
    return 1

if __name__ == '__main__':
    RES = take_pic()
    print(RES)
