import serial
import os
import re
import subprocess

firstFixFlag = False # this will go true after the first GPS fix.
firstFixDate = ""

# Set up serial:
ser = serial.Serial(
    port='/dev/ttyUSB0',\
    baudrate=4800,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=1)


# Helper function to take a $GPRMC sentence, and turn it into a Python dictionary.
# This also calls degrees_to_decimal and stores the decimal values as well.
def parse_GPRMC(data):
    data = data.split(',')
    dict = {
            'fix_time': data[1],
            'validity': data[2],
            'latitude': data[3],
            'latitude_hemisphere' : data[4],
            'longitude' : data[5],
            'longitude_hemisphere' : data[6],
            'speed': data[7],
            'true_course': data[8],
            'fix_date': data[9],
            'variation': data[10],
            'variation_e_w' : data[11],
            'checksum' : data[12]
    }
    dict['decimal_latitude'] = degrees_to_decimal(dict['latitude'], dict['latitude_hemisphere'])
    dict['decimal_longitude'] = degrees_to_decimal(dict['longitude'], dict['longitude_hemisphere'])
    return dict

def get_coord():
    line = ser.readline()
    if "$GPRMC" in line: # This will exclude other NMEA sentences the GPS unit provides.
        gpsData = parse_GPRMC(line) 
        print(gpsData['fix_date'] + "," + gpsData['fix_time'] + "," + str(gpsData['decimal_latitude']) + "," + str(gpsData['decimal_longitude']) +"\n")
        coord = ""+str(gpsData['decimal_latitude'])+","+str(gpsData['decimal_longitude'])+""
        return(coord)



def detect_gps():
        device_re = re.compile("Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
        df = subprocess.check_output("lsusb")
        devices = []
        for i in df.split('\n'):
            if i:
                info = device_re.match(i)
                if info:
                    dinfo = info.groupdict()
                    dinfo['device'] = '/dev/bus/usb/%s/%s' % (dinfo.pop('bus'), dinfo.pop('device'))
                    devices.append(dinfo)
        GPS = False
        j = 0
        for i in df.split('\n'):
                try :
                        if "Prolific Technology, Inc. PL2303 Serial Port" in (devices[j]["tag"]):
                                print("GPS DETECTED")
                                GPS = True
                        j = j + 1
                except :
                        pass

        return GPS

print(detect_gps())
print(get_coord())
