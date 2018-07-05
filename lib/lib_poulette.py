#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Librairie de lecture capteur'''
import sys
sys.path.append('../')


import random, time, platform

SYSTEM = platform.system()
if SYSTEM == 'Darwin':
    from lib_mac_SPI import *
    from lib_mac_water import libWater
else:
    from lib_SPI import *
    from lib_water import libWater

water = libWater()

ALERT_PROPRE = 20
ALERT_GRISE = 60
ALERT_BATTERY = 12

def get_temperature():
    '''read temp'''
    value1 = temp_int()
    value2 = temp_ext()
    value3 = temp_frigo()
    return value1, value2, value3

def get_humidity():
    '''read humidity'''
    value1 = hum_int()  
    value2 = hum_ext()
    return value1, value2

def get_water():
    '''read water'''
    print("readwater")
    value1 = water.eau_propre()
    value2 = water.eau_grise()
    return value1, value2

def get_battery():
    '''read battery'''
    value = bat_route()
    return value

def get_all():
    '''read all value'''
    temperature = get_temperature()
    humidity = get_humidity()
    water = get_water()
    battery = get_battery()
    return temperature, humidity, water, battery

def get_alert():
    '''return alert on water and battery '''
    water = get_water()
    battery = get_battery()
    res = []
    if water[0] <= ALERT_PROPRE:
        res.append("<h4>Alerte niveau eau propre</h4>")
    if water[1] >= ALERT_GRISE:
        res.append("<h4>Alerte niveau eau grise</h4>")
    if battery <= ALERT_BATTERY:
        res.append("<h4>Alerte niveau batterie</h4>")
    if res == []:
        res.append("<h4>Aucune alerte</h4>")
    return res

if __name__ == '__main__':
    print(get_alert())
