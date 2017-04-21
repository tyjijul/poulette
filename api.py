import time, datetime, random, subprocess
import csv, sys, os, requests, zipfile
from flask import Flask, session,send_file, render_template,redirect, url_for, request, jsonify, Markup, flash , Response
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
# from reconstruction.Reconstruction_SPGL1_EL import reconstructionSPGL1
# from reconstruction.analyse_par_block import analyse_block
# from reconstruction.analyse_par_block_juju import analyse_block2
# from multiprocessing import Process, Value, Array
# from csv_manager import update_csv_history
# import urllib.request as urllib2
from lib.lib_poulette import *
from geopy.geocoders import Nominatim
from lib.camera import VideoCamera

app = Flask(__name__)
app.secret_key = 'evo2000'
CORS(app, origins='http://192.168.1.92:8000')
api = Api(app)
IP = "10.55.1.62"

geolocator = Nominatim()
PATH_TO_IMG = "experience/img/"
#PATH = "/home/pi/poulette/"
PATH = "./"

#TAB = ["00001_photo.jpg","00002_photo.jpg","00003_photo.jpg","00004_photo.jpg","00005_photo.jpg","00006_photo.jpg","00007_photo.jpg","00008_photo.jpg","00010_photo.jpg","00011_photo.jpg","00012_photo.jpg","00013_photo.jpg","00014_photo.jpg","00015_photo.jpg","00016_photo.jpg","00017_photo.jpg","00018_photo.jpg","00019_photo.jpg","00020_photo.jpg","00021_photo.jpg","00022_photo.jpg","00023_photo.jpg","00024_photo.jpg","00025_photo.jpg","00026_photo.jpg","00027_photo.jpg","00028_photo.jpg","00029_photo.jpg"]

#Page d'accueil
@app.route('/')
def accueil():
    initSession()
    if session['start'] == 1:
        session['start'] = 0
        #session['TAB'] = TAB
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
    session['TAB'] = os.listdir('static/img') 
    return render_template('gallery.html')

#Route map : 
@app.route('/map', methods = ['GET', 'POST'])
def map():
    return render_template('map.html')


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

#Fonction AJAX WEATHER
@app.route('/weather', methods = ['POST'])
def ajax_weather():
    print(PATH+'GPS-log.txt')
    gpsFile = open(PATH+'GPS-log.txt')
    temp = gpsFile.readline() 
    gpsFile.close()
    value = temp.split(",")   
    t1 = value[2] #= 48.3581516667
    t2 = value[3] #= -4.56562166667
    print("VALUE")
    print(t1)
    print(t2)
    location = geolocator.reverse(""+str(t1)+","+str(t2)+"")
    res = location.raw['address']['county']
    return jsonify(CITY=res, LAT=t1, LONG=t2)

#Fonction AJAX LOCATION
@app.route('/location', methods = ['POST'])
def ajax_location():
    gpsFile = open(PATH+'GPS-log.txt')
    temp = gpsFile.readline() 
    gpsFile.close()
    value = temp.split(",")   
    t1 = value[2]
    t2 = value[3]
    return jsonify(LAT=t1, LONG=t2)

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


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    #return Response(gen(VideoCamera()),mimetype='multipart/x-mixed-replace; boundary=frame')
    return jsonify(out=1)

############# MICROBS ################################
#Fonction AJAX nom expérience
# @app.route('/name/1', methods = ['POST'])
# def ajax_request():
#     username = request.form['username']
#     session['name'] = username
#     return jsonify(username=username )    

# #Route vers SUCCEES
# @app.route('/startAcq')
# def ajax_acq():
#     session['duree_experience'] = str(datetime.datetime.now() - session['debut'])
#     session['nombre_bacterie'] = tmp_bact.value
#     historiqueCSV()
#     return render_template('success.html', error = "error")

# #Route vers ACQUISITION
# @app.route('/acquisition', methods = ['GET', 'POST'])
# def acquisition():
#     session['date'] = time.strftime("%Y-%m-%d_%H:%M:%S_")
#     session['debut'] = datetime.datetime.now()
#     global tmp_bact
#     tmp_bact = Value('i',0)
#     global proc
#     proc = Process(target=process_run, args=(session['name'],tmp_bact, ))
#     proc.start()

#     error = "Veuillez patienter"
#     return render_template('acquisition.html', error = error)

# #Fonction AJAX process exist ? 
# @app.route('/status')
# def thread_status():
#     finished = proc.is_alive()
#     print("finished = "+str(finished))
#     return jsonify(dict(status=('finished' if not finished else 'running')))

# #Fonction AJAX avancement reconstruction :
# @app.route('/status_txt')
# def thread_status_txt():
#     file = open("statefile.txt", "r") 
#     info_txt = file.readline()
#     file.close()
#     print(info_txt)
#     return jsonify(dict(status=(info_txt)))

# #Route vers annulation reconstruction : 
# @app.route('/cancel', methods = ['GET', 'POST'])
# def cancel():
#     proc.terminate()
#     return render_template('index.html')

# #Route vers download :
# @app.route('/download', methods = ['GET', 'POST'])
# def download():
#     fileNAME = createCSV()
#     zipf = zipfile.ZipFile(fileNAME+'.zip','w', zipfile.ZIP_DEFLATED)
#     print(os.system('ls'))
#     #zipf.write(''+session['img'])
#     zipf.write('src/data/M_signal_use_08.txt')
#     zipf.write('src/data/M_phi_use_08.mat')
#     zipf.close()
#     return send_file('../Name.zip',mimetype = 'zip',attachment_filename= 'Name.zip',as_attachment = True)

# #Fonction historique CSV : 
# def historiqueCSV():
#     newline = [session['name'] , session['date']   , session['duree_experience']  , session['nombre_bacterie'], session['range1'] , session['range2'] , session['data_1024']  , session['data_256']   , session['data_64'], session['img_final']  , session['img_binarisee']  , session['version_algorithme']]
#     update_csv_history(newline)

# #Fonction création CSV :
# def createCSV():
#     c = csv.writer(open("experience/"+session['date']+session['name']+".csv", "w"))
#     c.writerow(["nom", "date", "duree_experience", "nombre_bacterie", "range1", "range2", "data_1024", "data_256", "data_64", "img_final", "img_binarisee", "version_algorithme"])
#     c.writerow((session['name'] , session['date']   , session['duree_experience']  , session['nombre_bacterie'], session['range1'] , session['range2'] , session['data_1024']  , session['data_256']   , session['data_64'], session['img_final']  , session['img_binarisee']  , session['version_algorithme']))
#     return str(session['date']+session['name'])
# #Fonction initialisation :  
def initSession():
    session.clear()
    session['start'] = 1
    session['date'] = "none"
    session['img'] = "none"
    session['range1'] = "none"
    session['range2'] = "none"
    session['duree_experience'] = "none"
    session['nombre_bacterie'] = "none"
    session['data_1024'] = "none"
    session['data_256'] = "none"
    session['data_64'] = "none"
    session['img_final'] = "none"
    session['img_binarisee'] = "none"
    session['version_algorithme'] = "V1.0" 


def getAllValue(): 
    value = get_temperature()
    session['temp1'] = value[0]
    session['temp2'] = value[1]
    session['temp3'] = value[2]
    

# @app.route('/historique')
# def historique():
#     initSession()
#     return render_template('historique.html')




if __name__ == "__main__":
    app.run(host='0.0.0.0')#,debug=True)






        
    
