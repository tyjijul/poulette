#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, datetime, random, subprocess, platform
import csv, sys, os, requests, zipfile
from flask import Flask, session,send_file, render_template,redirect, url_for, request, jsonify, Markup, flash , Response
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
from lib_poulette import *
from geopy.geocoders import Nominatim
from camera import VideoCamera
from lib_GPS import *
from lib_picture import *

app = Flask(__name__)
app.secret_key = 'evo2000'
CORS(app, origins='http://192.168.1.92:8000')
api = Api(app)
IP = "10.55.1.62"
geolocator = Nominatim()

SYSTEM = platform.system()
if SYSTEM == 'Darwin':
    PATH = "/home/pi/poulette/"
else:
    PATH = "./"


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
    return render_template('index.html')

#Route camera : 
@app.route('/camera', methods = ['GET', 'POST'])
def camera():
    session['TAB'] = sorted(os.listdir('static/img') , key=str.lower, reverse=True)
    return render_template('gallery.html')

#Route map : 
@app.route('/map', methods = ['GET', 'POST'])
def map():
    return render_template('map.html')

#Route map : 
@app.route('/mapL', methods = ['GET', 'POST'])
def mapL():
    return render_template('mapL.html')

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
    print(value)
    return jsonify(alert=value)

#Fonction AJAX WEATHER
@app.route('/weather', methods = ['POST'])
def ajax_weather():
    try:
        T = get_town()
    except(ValueError):
        print("//////////////////////e.code")
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
    print("PHOTO PRISE !!!!!")
    return jsonify(out="1")

#Fonction PICTURE
@app.route('/Mail_picture', methods = ['POST'])
def mail_picture():
    username = request.form['username']
    print("SENDING BY MAIL !!!!!")
    print(username)
    send_mail_pic(username)
    return jsonify(out="1")

#Fonction PICTURE
@app.route('/SMS_picture', methods = ['POST'])
def sms_picture():
    take_pic()
    print("SENDING BY SMS !!!!!")
    return jsonify(out="1")

#Fonction check GIT update
@app.route('/update', methods = ['POST'])
def update():
    output = subprocess.check_output(PATH+"git_status.sh", shell=True)
    if b'Up-to-date' in output : 
        print("up-to-date")
        out = "True"
    else : 
        print("update available")
        out = "False"
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


def initSession():
    session.clear()
    session['start'] = 1
    session['temp1'] =  None
    session['temp2'] =  None
    session['temp3'] =  None
    session['hum1'] =   None
    session['hum2'] =   None
    session['water1'] = None
    session['water2'] = None
    session['bat1'] = None

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
    app.run(host='0.0.0.0')#,debug=True)






        
    
