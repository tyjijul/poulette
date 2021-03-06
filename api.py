#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time, datetime, random, subprocess, platform
import csv, sys, os, requests, zipfile, glob
sys.path.insert(0, 'lib')
from flask import Flask, session,send_file, render_template,redirect, url_for, request, jsonify, Markup, flash , Response
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
from multiprocessing import Process, Event, Lock
from lib_poulette import *
from lib_tracking import *
from lib_json import libJson
from geopy.geocoders import Nominatim
import requests, json
#from lib_mail import *
from lib_GPS import *

# de la merde pour modifier le git haha haha haha hahahahaha

app = Flask(__name__)
app.secret_key = 'evo2000'
# app.config['SERVER_NAME'] = "test.dev:5000"
CORS(app, origins='http://192.168.1.92:8000')
api = Api(app)
IP = "10.55.1.62"
geolocator = Nominatim()
IMG_PATH = "static/img/"

# de la merde pour merger

lj = libJson()

SYSTEM = platform.system()
if SYSTEM == 'Darwin':
    PATH = "/home/pi/poulette/"
    from lib_mac_picture import *
else:
    PATH = "./"
    from lib_picture import *
    from camera import VideoCamera


#Page d'accueil
@app.route('/')
def accueil():
    initSession()
    if session['start'] == 1:
        session['start'] = 0
        getAllValue()
    return render_template('index.html')

#Route Niveau : 
@app.route('/niveau', methods = ['GET', 'POST'])
def niveau():
    return render_template('gauge.html')

#Route anchor : 
@app.route('/anchor', methods = ['GET', 'POST'])
def anchor():
    session['P4N'] = [("t1", "para1", "pic1"),("t2", "para2", "pic2"),("t3", "para3", "pic3")]
    return render_template('anchor.html')

#Route camera : 
@app.route('/camera', methods = ['GET', 'POST'])
def camera():
    session['TAB'] = sorted(os.listdir('static/img') , key=str.lower, reverse=True)
    return render_template('gallery.html')

#Route map : 
@app.route('/map', methods = ['GET', 'POST'])
def map():
    return render_template('map.html')


#Route param : 
@app.route('/param', methods = ['GET', 'POST'])
def param():
    return render_template('param.html')

#Route tracker : 
@app.route('/tracker', methods = ['GET', 'POST'])
def tracker():
    data = {'holidayTXT': session['holiday'], 'holidayStart': session['holidayStart']}
    listgps = sorted(glob.glob("static/gps/20*") , key=str.lower, reverse=True)
    GPS = []
    dataGPS = []
    for datas in listgps:
        slip = datas.split("/")
        parse = slip[2].split("-")
        dataGPS.append(parse[0])
        dataGPS.append(parse[1])
        GPS.append(dataGPS)
        dataGPS=[]
        session['GPS'] = GPS
    return render_template('tracker.html', points=json.dumps(data))

#Fonction AJAX TEMP
@app.route('/temp', methods = ['POST'])
def ajax_temp():
    value = get_temperature()
    return jsonify(T1=value[0], T2=value[1], T3=value[2])

#Fonction AJAX BATTERY
@app.route('/battery', methods = ['POST'])
def ajax_bat():
    value = get_battery()
    return jsonify(T1=value)

#Fonction AJAX EAU
@app.route('/water', methods = ['POST'])
def ajax_water():
    value = get_water()
    return jsonify(T1=value[0], T2=value[1])

#Fonction AJAX HUMIDITE
@app.route('/hum', methods = ['POST'])
def ajax_hum():
    value = get_humidity()
    return jsonify(T1=value[0], T2=value[1])

#Fonction AJAX ALERT 
@app.route('/alertUpdate', methods = ['POST'])
def ajax_alert():
    value = get_alert()
    return jsonify(alert=value)

#Fonction AJAX WEATHER
@app.route('/weather', methods = ['POST'])
def ajax_weather():
    try:
        T = get_town()
    except(ValueError):
        return jsonify(CITY=0, LAT=0, LONG=0)
    return jsonify(CITY=T[0], LAT=T[1], LONG=T[2])

#Fonction AJAX LOCATION
@app.route('/location', methods = ['POST'])
def ajax_location():
    T = get_coord()
    return jsonify(LAT=T[0], LONG=T[1])

#Fonction PICTURE
@app.route('/picture', methods = ['POST'])
def take_picture():
    take_pic()
    return jsonify(out="1")

# Fonction send picture
@app.route('/Download_picture/<N>', methods = ['GET', 'POST'])
def Download_picture(N):
    return send_file(IMG_PATH+N,mimetype = 'jpg',attachment_filename= N,as_attachment = True)


#Fonction PICTURE
@app.route('/Mail_picture', methods = ['POST'])
def mail_picture():
    username = request.form['username']
    mail = request.form['email']
    mail_process = Process(target=sendEmail, args=(username, mail, session['name']))
    mail_process.start()
    return jsonify(out="1")

#Fonction PICTURE
@app.route('/Delete_picture', methods = ['POST'])
def delete_picture():
    username = request.form['username']
    del_pic(username)
    return jsonify(out="1")

#Fonction check GIT update
@app.route('/update', methods = ['POST'])
def update():
    output = subprocess.check_output("./git_status.sh", shell=True)
    if b'not-up-to-date' in output: 
        print("flask: not-up-to-date")
        out = "False"
    elif b'up-to-date' in output : 
        print("flask: up-to-date")
        out = "True"
    else : 
        print("Error git status")
        out = "True"
    return jsonify(out=out)

#Generation d'image provenant de la camera 
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

#Envoie des images au client web
@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/download/<N>', methods = ['GET', 'POST'])
def download(N):
    return send_file("static/gps/"+N,mimetype = 'txt',attachment_filename= N,as_attachment = True)

#Fonction MAIL GPX
@app.route('/Mail_gpx', methods = ['POST'])
def mail_gpx():
    username = request.form['username']
    mail = request.form['email']
    mail_process = Process(target=sendEmailGpx, args=(username, mail, session['name']))
    mail_process.start()
    return jsonify(out="1")

#Fonction DELETE GPX
@app.route('/del_gpx', methods = ['POST'])
def del_gpx():
    username = request.form['username']
    removeGpx(username)
    return jsonify(out="1")


@app.route('/Holiday/<N>', methods = ['GET', 'POST'])
def holiday(N):
    print("api.py : N = "+N)
    username = request.form['username']
    print("api.py : username = "+username)    
    if N != "tmp":
        if N == "1":
            session['holiday'] = 0
            is_holyday(int(N), username)
        elif N == "0":
            session['holiday'] = 1
            is_holyday(int(N), "#")
        with open("holiday.txt", "r") as holiday : 
            line = holiday.readline()
            parseholiday = line.split(";")
            if parseholiday[0] == "1":
                session['holiday'] = 1
                print("api.py : C'EST LES VACANCES !!!!!!")
            else :
                session['holiday'] = 0
                print("api.py : AU BOULOT !!!!!!")
            session['holidayStart'] = parseholiday[1]
    else :
        with open("holiday.txt", "r") as holiday : 
            line = holiday.readline()
            parseholiday = line.split(";")
        print(parseholiday[1])
        is_holyday(2, parseholiday[2])
    return jsonify(out="1")


@app.route('/update_param', methods = ['POST'])
def update_param():
    username = request.form['username']
    lj.change_key('name',username)
    return jsonify(out="1")

@app.route('/reboot', methods = ['POST'])
def reboot():
    os.system('sudo shutdown -r now')
    return jsonify(out="1")

@app.route('/gitPull', methods = ['POST'])
def gitPull():
    os.system('git pull')
    return jsonify(out="1")
    
def initSession():
    session.clear()
    session['start'] = 1
    session['name'] = lj.read_key('name')
    session['temp1'] =  None
    session['temp2'] =  None
    session['temp3'] =  None
    session['hum1'] =   None
    session['hum2'] =   None
    session['water1'] = None
    session['water2'] = None
    session['bat1'] = None
    with open("holiday.txt", "r") as holiday : 
        line = holiday.readline()
        parseholiday = line.split(";")
        if parseholiday[0] == "1":
            session['holiday'] = 1
            print("api.py : C'EST LES VACANCES !!!!!!")
        else :
            session['holiday'] = 0
            print("api.py : AU BOULOT !!!!!!")
        session['holidayStart'] = parseholiday[1]

def getAllValue():
    value = get_all()
    session['temp1'] =  value[0][0]
    session['temp2'] =  value[0][1]
    session['temp3'] =  value[0][2]
    session['hum1'] =   value[1][0]
    session['hum2'] =   value[1][1]
    session['water1'] = value[2][0]
    session['water2'] = value[2][1]
    session['bat1'] = value[3]

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)






        
    
