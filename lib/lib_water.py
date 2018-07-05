#!/usr/bin/python
# encoding: utf-8
import sys
sys.path.append('../')
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# PROGRAMME DE CALCUL DE NIVEAU D'EAU :						#
#															#
#	-GPIO 23 (p4) 	-->  	vide (bas)						#
#	-GPIO 22 (p3) 	--> 	1/4  (quart)					#
#	-GPIO 27 (p2) 	--> 	1/2  (milieu)					#
#	-GPIO 18 (p1) 	--> 	3/4  (haut)						#
#	-GPIO 17 (P0)	--> 	4/4  (plein)					#
#	-GPIO 25 (p5) 	-->  Alimentation EAU PROPRE			#
#	-GPIO 4  (p6) 	-->  Alimentation EAU vide 				#
#															#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import RPi.GPIO as GPIO
import time
                                                            
class libWater():
	def __init__(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup(23,GPIO.IN)		#Gauge vide
		GPIO.setup(22,GPIO.IN)		#Gauge 1/4
		GPIO.setup(27,GPIO.IN)		#Gauge 1/4
		GPIO.setup(18,GPIO.IN)		#Gauge 1/4
		GPIO.setup(17,GPIO.IN)		#Gauge 1/4
		GPIO.setup(25,GPIO.OUT) 	#activation gauge
		GPIO.output(25,GPIO.LOW)	#init low 
		GPIO.setup(4,GPIO.OUT) 	#activation gauge
		GPIO.output(4,GPIO.LOW)	#init low 



	def eau_propre(self):
		GPIO.output(25,GPIO.HIGH)

		res = GPIO.input(17)
		res = res + GPIO.input(18)
		res = res + GPIO.input(27)
		res = res + GPIO.input(22)
		res = res + GPIO.input(23)

		GPIO.output(25,GPIO.LOW)

		if(res == 5):
			print("Le niveau d'eau propre est supérieur au trois quart")
			res = 100
		elif(res == 4):
			print("Le niveau d'eau propre est au trois quart")
			res = 75
		elif(res == 3):
			print("Le niveau d'eau propre est à la moitié")
			res = 50
		elif(res == 2):
			print("Le niveau d'eau propre est au quart")
			res = 25
		elif(res == 1):
			print("Le niveau d'eau est CRITIQUE !!!!!")
			res = 10
		else:
			print("Il n'y a plus d'eau dans le réservoir")
			res =0
		return res


	def eau_grise(self):
		GPIO.output(4,GPIO.HIGH)

		res = GPIO.input(17)
		res = res + GPIO.input(18)
		res = res + GPIO.input(27)
		res = res + GPIO.input(22)
		res = res + GPIO.input(23)

		GPIO.output(4,GPIO.LOW)

		if(res == 5):
			print ("Le niveau d'eau propre est supérieur au trois quart")
			res = 100
		elif(res == 4):
			print ("Le niveau d'eau propre est au trois quart")
			res = 75
		elif(res == 3):
			print ("Le niveau d'eau propre est à la moitié")
			res = 50
		elif(res == 2):
			print ("Le niveau d'eau propre est au quart")
			res = 25
		elif(res == 1):
			print ("Le niveau d'eau est CRITIQUE !!!!!")
			res = 10
		else:
			print ("Il n'y a plus d'eau dans le réservoir")
			res =0
		return res


