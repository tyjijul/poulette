# #!/usr/bin/env python

# from multiprocessing import Process, Pool
# import time
# import urllib.request as urllib2

# def millis():
#   return int(round(time.time() * 1000))

# def http_get():
#   start_time = millis()
#   result = "bim"
#   print("bim")
#   #result = {"url": 'http://10.55.1.62:5000/video', "data": urllib2.urlopen('http://10.55.1.62:5000/video', timeout=10).read()[:100]}
  
#   response = urllib2.urlopen('http://10.55.1.62:5000/video')
#   html = response.read()
#   result = urllib2.urlopen('http://10.55.1.62:5000/video', timeout=10).read(100)
#   #print('http://10.55.1.62:5000/video' + " took " + str(millis() - start_time) + " ms")
#   return response
  
# #urls = ['http://10.55.1.62:5000/video', 'https://foursquare.com/', 'http://www.yahoo.com/', 'http://www.bing.com/', "https://www.yelp.com/"]

# #pool = Pool(processes=1)

# #response = urllib2.urlopen('http://10.55.1.62:5000/video')
# start_time = millis()
# #results = pool.map(http_get, urls)
# results = Process(target = http_get)
# print("\nTotal took " + str(millis() - start_time) + " ms\n")

# #for result in results:
# print(results)


import threading
import urllib.request as urllib2
import time
from multiprocessing import Process
from reconstruction.Reconstruction_SPGL1_EL import reconstructionSPGL1
from reconstruction.analyse_par_block import analyse_block
import urllib.request as urllib2
import os

start = time.time()
url = ["http://www.google.com", "http://www.apple.com", "http://www.facebook.com"]

def fetch_url(url):
    urlHandler = urllib2.urlopen("http://10.55.1.62:5000/video")
    html = urlHandler.content()
    print("'%s\' fetched in %ss" % (html, (time.time() - start)))

#threads = [Process(target=fetch_url, args=(url,)) for url in urls]
#thread = Process(target=fetch_url, args=(url,))
#for thread in threads:
#thread.start()
IP = "10.55.1.62"
#res = urllib2.urlopen('http://'+IP+':5000/flag/on')        # Flag ON
#res = urllib2.urlopen('http://'+IP+':5000/video')          # Start video 1092x1092 
#res = urllib2.urlopen('http://'+IP+':5000/flag/off')       # Flag OFF 
# ####### GET DATA FROM I2C FUNCTION ###########
#update_state("Reconstruction SPGL")
name = "ddd.jpg"
#path = os.path.join(os.path.expanduser('~'), 'documents', 'python', name)
#print(path)
#IMGname = reconstructionSPGL1(name,'data/M_phi_use_08.mat', 'data/M_signal_use_08.txt')
print(os.system("pwd"))
coord = analyse_block("../ddd.jpg")      
#for thread in threads:
#    thread.join()

#print("Elapsed Time: %s" % (time.time() - start))



