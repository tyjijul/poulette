
#infile = open("photo-log.txt", "r")
#for line in open("photo-log.txt", "r"): print(line)

import os
TAB = os.listdir('static/img') 
#TAB = ["00001_photo.jpg","00002_photo.jpg","00003_photo.jpg","00004_photo.jpg","00005_photo.jpg","00006_photo.jpg","00007_photo.jpg"]
for line in  TAB : print(line)