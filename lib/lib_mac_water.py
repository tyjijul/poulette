#!/usr/bin/python
# encoding: utf-8

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

import sys
sys.path.append('../')
                                                            
class libWater():
	def __init__(self):
		print("init water")



	def eau_propre(self):
		res = 50
		return res


	def eau_grise(self):
		res = 50
		return res


