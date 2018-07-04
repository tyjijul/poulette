#!/usr/bin/env python
# -*- coding: utf-8 -*-

from geopy.geocoders import Nominatim

geolocator = Nominatim()


def get_coord():
    gpsFile = open('GPS-log.txt')
    temp = gpsFile.readline()
    gpsFile.close()
    value = temp.split(",")
    t1 = value[2] #= 48.3581516667
    t2 = value[3] #= -4.56562166667
    #location = geolocator.reverse(""+str(t1)+","+str(t2)+"")
    #res = " "+location.raw['address']['town']
    return(t1,t2)

def get_town():
    coord = get_coord()
    # try : 
    location = geolocator.reverse(""+str(coord[0])+","+str(coord[1])+"")
    # except : 
    #     raise ValueError("Problème de connexion internet essayer plus tard")
    try:
        res = " "+location.raw['address']['village']
    except:
        try:
            res = " "+location.raw['address']['county']
        except:
            res = " "+location.raw['address']['town']
    return(res, coord[0], coord[1])
    
if __name__ == '__main__':
    COORD = get_coord()
    print(COORD)
    TOWN = get_town()
    print(TOWN)

