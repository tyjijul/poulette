import time, datetime, random
import csv, sys, os, requests, zipfile
from flask import Flask, session,send_file, render_template,redirect, url_for, request, jsonify, Markup, flash
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
# from reconstruction.Reconstruction_SPGL1_EL import reconstructionSPGL1
# from reconstruction.analyse_par_block import analyse_block
# from reconstruction.analyse_par_block_juju import analyse_block2
# from multiprocessing import Process, Value, Array
# from csv_manager import update_csv_history
# import urllib.request as urllib2
from geopy.geocoders import Nominatim

app = Flask(__name__)
app.secret_key = 'evo2000'
CORS(app, origins='http://192.168.1.92:8000')
api = Api(app)
IP = "10.55.1.62"

geolocator = Nominatim()

PATH_TO_IMG = "experience/img/"

# def update_state(txt):
#     file = open("statefile.txt","w") 
#     file.write(txt) 
#     file.close()
        
# def process_run(name, bact):
#     update_state("Diffusion pattern 1024px")
#     ####### START VIDEO 1024 #####################
#     res = urllib2.urlopen('http://'+IP+':5000/flag')        # Flag ON
#     res = urllib2.urlopen('http://'+IP+':5000/video')          # Start video 1092x1092 
#     res = urllib2.urlopen('http://'+IP+':5000/flag')        # Flag ON
#     ####### GET DATA FROM I2C FUNCTION ###########
#     update_state("Reception des données")
#     time.sleep(2)
#     ####### RECONSTRUCTION #######################
#     update_state("Reconstruction SPGL")
#     IMGname = reconstructionSPGL1(PATH_TO_IMG, name,'src/data/M_phi_use_08.mat', 'src/data/M_signal_use_08.txt')
#     coord = analyse_block2(PATH_TO_IMG + name+".jpg")
#     print(coord)
#     #coord = [[16, 0],[32, 0]]
#     bact.value = len(coord)
#     for i in range(len(coord)):                                         # Pour chaque coordonnées
#         update_state("Analyse par block 64px, nombre de bactérie(s) : "+str(i+1)+"/"+str(len(coord)))
#         res = urllib2.urlopen('http://'+IP+':5000/flag')             # Flag ON
#         res = urllib2.urlopen('http://'+IP+':5000/play/'+str(int(coord[i][0])*16)+'/'+ str(int(coord[i][1])*16))
#         res = urllib2.urlopen('http://'+IP+':5000/flag')            # Flag OFF
#     #   Reception des données 
#     # #
#     # # Traitement 
#     t2 = datetime.datetime.now()
#     #session['duree_experience'] = str(t2-t1)
#     # # CREATION DE FICHIER CSV
#     #session['fileNAME'] = createCSV()


#Page d'accueil
@app.route('/')
def accueil():
    initSession()
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
    return render_template('index.html')

#Route map : 
@app.route('/map', methods = ['GET', 'POST'])
def map():
    return render_template('map.html')


#Fonction AJAX TEMP
@app.route('/temp', methods = ['POST'])
def ajax_temp():
    t1 = round(random.uniform(-20, 40),2)
    t2 = round(random.uniform(-20, 40),2)
    t3 = round(random.uniform(-20, 40),2)
    return jsonify(T1=t1, T2=t2, T3=t3)

#Fonction AJAX BATTERY
@app.route('/battery', methods = ['POST'])
def ajax_bat():
    t1 = round(random.uniform(9, 15),2)
    print(t1)
    return jsonify(T1=t1)

#Fonction AJAX EAU
@app.route('/water', methods = ['POST'])
def ajax_water():
    print("wheeeee")
    t1 = random.randint(0,100)
    t2 = random.randint(0,100)
    return jsonify(T1=t1, T2=t2)

#Fonction AJAX HUMIDITE
@app.route('/hum', methods = ['POST'])
def ajax_hum():
    t1 = random.randint(0,100)
    t2 = random.randint(0,100)
    return jsonify(T1=t1, T2=t2)

#Fonction AJAX WEATHER
@app.route('/weather', methods = ['POST'])
def ajax_weather():
    t1 = 48.8588443
    t2 = 2.8588443
    location = geolocator.reverse(""+str(t1)+","+str(t2)+"")
    res = location.raw['address']['county']
    return jsonify(CITY=res, LAT=t1, LONG=t2)





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
    session['name'] = "none"
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

# @app.route('/historique')
# def historique():
#     initSession()
#     return render_template('historique.html')




if __name__ == "__main__":
    app.run(host='0.0.0.0')#,debug=True)






        
    
